#!/usr/bin/env python3
"""Final canonical CPU solver path for the LCST hydrogel model.

This module refactors the migrated legacy CPU solver into an auditable
canonical path. It preserves the legacy v0 trajectory as a controlled
non-canonical branch while fixing the paper-solver defaults chosen in issue
#15.

No model or claim is validated by this module.
"""

from __future__ import annotations

import json
import platform
import subprocess
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Dict, Tuple

import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
from scipy.sparse import csc_matrix, lil_matrix


SOURCE_SCALING_CHOICES = {
    "current_volume",
    "reference_volume",
    "diagnostic_J_beta",
}
CHI_CLOSURE_CHOICES = {
    "effective_osmotic_chi",
    "strict_chi_derivative",
}
TRANSPORT_CLOSURE_CHOICES = {
    "legacy_porosity_power",
    "normalized_porosity_power",
    "constant_no_barrier",
    "accessibility_constant",
    "transport_constant",
    "diffusivity_constant",
    "mobility_constant",
}
FLOOR_SCHEME_CHOICES = {"legacy", "canonical_consistent"}
BOUNDARY_SCHEME_CHOICES = {"cell_center_robin"}


@dataclass
class CanonicalParams:
    """Parameter set for the final canonical CPU solver path."""

    N: int = 51
    t_end: float = 300.0
    n_save: int = 3000
    method: str = "BDF"
    rtol: float = 1.0e-6
    atol: float = 1.0e-8
    max_step: float = 0.5

    source_scaling: str = "reference_volume"
    source_J_exponent: float = 0.0
    chi_closure: str = "effective_osmotic_chi"
    transport_closure: str = "normalized_porosity_power"
    floor_scheme: str = "canonical_consistent"
    boundary_scheme: str = "cell_center_robin"
    enthalpy_advection: bool = False

    phi_p0: float = 0.15
    chi_inf: float = 0.60
    S_chi: float = 1.00
    chi1: float = 1.10
    Omega_e: float = 0.12
    ell: float = 0.01

    Da: float = 4.0
    delta: float = 0.08
    alpha: float = 0.20
    Gamma_A: float = 1.5
    eps_T: float = 0.03
    arrh_exp_cap: float = 60.0

    use_hill: bool = False
    theta_c: float = 0.5
    n_hill: float = 4.0
    hill_eps: float = 0.05

    Bi_mu: float = 1.00
    Bi_c: float = 0.70
    Bi_T: float = 0.10
    B_vol: float = 0.0
    B_Tvol: float = 0.0
    Bi_c_vol: float = 0.0
    Bi_J_vol: float = 0.0
    m_b: float = 0.0
    auto_set_m_b: bool = True

    m_act: float = 6.0
    m_diff: float = 2.0
    m_mob: float = 1.0
    reaction_order: float = 1.0

    a_floor: float = 0.0
    d_floor: float = 0.0
    mu_floor: float = 0.0
    A_min: float = 1.0e-4
    D_min: float = 1.0e-4
    M_min: float = 1.0e-4
    closure_form: str = "power"
    beta_free_volume: float = 8.0
    M0: float = 1.0
    D0: float = 2.0
    C0: float = 1.0
    K0: float = 1.0
    Pe_T: float = 0.0
    Theta_infty: float = 33.3333333333

    J_init: float = 1.30
    u_init: float = 0.02
    theta_init: float = 0.0
    eps_J: float = 5.0e-3
    eps_u: float = 5.0e-3
    eps_theta: float = 1.0e-4

    J_min: float = 0.153
    J_max: float = 6.0
    u_floor: float = 1.0e-12
    phi_floor: float = 1.0e-10
    phi_ceiling: float = 0.995
    theta_clip: float = 25.0


def _require_choice(name: str, value: str, choices: set[str]) -> None:
    if value not in choices:
        raise ValueError(f"{name}={value!r} is not one of {sorted(choices)}")


def validate_params(p: CanonicalParams) -> None:
    _require_choice("source_scaling", p.source_scaling, SOURCE_SCALING_CHOICES)
    _require_choice("chi_closure", p.chi_closure, CHI_CLOSURE_CHOICES)
    _require_choice("transport_closure", p.transport_closure, TRANSPORT_CLOSURE_CHOICES)
    _require_choice("floor_scheme", p.floor_scheme, FLOOR_SCHEME_CHOICES)
    _require_choice("boundary_scheme", p.boundary_scheme, BOUNDARY_SCHEME_CHOICES)
    if p.enthalpy_advection:
        raise ValueError(
            "enthalpy_advection=True is not implemented in the candidate "
            "canonical solver; Pe_T is diagnostic-only in this branch."
        )
    if p.J_min <= 0.0 or p.J_max <= p.J_min:
        raise ValueError("Require 0 < J_min < J_max.")
    if not (0.0 < p.phi_ceiling < 1.0):
        raise ValueError("Require 0 < phi_ceiling < 1.")
    if not np.isfinite(p.source_J_exponent):
        raise ValueError("source_J_exponent must be finite.")


def active_numerical_bounds(p: CanonicalParams) -> Dict[str, float]:
    """Return the actual positivity/projection bounds used by the solver."""
    active_J_min = max(float(p.J_min), float(p.phi_p0) / float(p.phi_ceiling))
    active_J_max = float(p.J_max)
    return {
        "J_min": active_J_min,
        "J_max": active_J_max,
        "logJ_min": float(np.log(active_J_min)),
        "logJ_max": float(np.log(active_J_max)),
        "phi_ceiling": float(p.phi_ceiling),
        "u_floor": float(p.u_floor),
        "arrh_exp_cap": float(p.arrh_exp_cap),
    }


def model_branch_labels(p: CanonicalParams) -> Dict[str, Any]:
    return {
        "source_scaling": p.source_scaling,
        "source_J_exponent": float(p.source_J_exponent),
        "chi_closure": p.chi_closure,
        "chi_parameter_interpretation": "effective_osmotic_interaction_parameter"
        if p.chi_closure == "effective_osmotic_chi"
        else "strict_free_energy_derivative_sensitivity",
        "transport_closure": p.transport_closure,
        "floor_scheme": p.floor_scheme,
        "boundary_scheme": p.boundary_scheme,
        "enthalpy_advection": bool(p.enthalpy_advection),
        "Pe_T_status": "omitted_from_rhs_by_model_assumption",
        "transport_metric_closure": "reference_metric"
        if p.transport_closure != "legacy_porosity_power"
        else "legacy_unmetricized",
        "canonical_paper_solver": bool(
            p.source_scaling == "reference_volume"
            and p.chi_closure == "effective_osmotic_chi"
            and p.transport_closure == "normalized_porosity_power"
            and p.floor_scheme == "canonical_consistent"
            and p.boundary_scheme == "cell_center_robin"
            and not p.enthalpy_advection
        ),
        "validation_status": "candidate_not_validated",
    }


def git_metadata(root: Path | None = None) -> Dict[str, Any]:
    root = root or Path(__file__).resolve().parents[3]

    def _run(args: list[str]) -> str | None:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=root,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            return result.stdout.strip()
        except Exception:
            return None

    status = _run(["status", "--short"])
    return {
        "commit": _run(["rev-parse", "HEAD"]),
        "branch": _run(["branch", "--show-current"]),
        "dirty": bool(status),
        "status_short": status or "",
    }


def source_file_hashes(root: Path | None = None) -> Dict[str, str | None]:
    root = root or Path(__file__).resolve().parents[3]
    paths = [
        "paper/solver/canonical_cpu/solver.py",
        "paper/solver/canonical_cpu/run_smoke_checks.py",
        "tests/test_canonical_solver.py",
    ]
    hashes: Dict[str, str | None] = {}
    for rel in paths:
        path = root / rel
        if not path.exists():
            hashes[rel] = None
            continue
        import hashlib

        hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def params_to_dict(p: CanonicalParams, finalized: bool = True) -> Dict[str, Any]:
    pp = finalize_params(p) if finalized else p
    payload = asdict(pp)
    payload["model_branches"] = model_branch_labels(pp)
    payload["solver"] = {
        "name": "canonical_cpu",
        "status": "final_paper_solver_evidence_generation_pending",
        "module": "paper.solver.canonical_cpu.solver",
    }
    payload["runtime"] = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": np.__version__,
    }
    payload["git"] = git_metadata()
    payload["source_file_sha256"] = source_file_hashes()
    return payload


def save_params_json(p: CanonicalParams, path: str | Path, finalized: bool = True) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        dumps_strict_json(params_to_dict(p, finalized=finalized)),
        encoding="utf-8",
    )


def _json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def _json_sanitize(value):
    if isinstance(value, dict):
        return {str(k): _json_sanitize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_sanitize(v) for v in value]
    if isinstance(value, np.ndarray):
        return _json_sanitize(value.tolist())
    if isinstance(value, np.generic):
        return _json_sanitize(value.item())
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    return value


def dumps_strict_json(payload: Dict[str, Any]) -> str:
    return json.dumps(
        _json_sanitize(payload),
        indent=2,
        sort_keys=True,
        default=_json_default,
        allow_nan=False,
    )


def save_run_bundle(
    data: Dict[str, Any],
    p: CanonicalParams,
    outdir: str | Path,
    run_name: str,
) -> Dict[str, Path]:
    """Persist arrays, finalized parameters, and diagnostics for one run.

    The saved files are intended for audit and smoke-test reproducibility, not
    as paper evidence.
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in run_name)
    params_path = outdir / f"{safe_name}_params.json"
    diagnostics_path = outdir / f"{safe_name}_diagnostics.json"
    arrays_path = outdir / f"{safe_name}_timeseries.npz"

    save_params_json(p, params_path)
    diagnostics = {
        "run_name": safe_name,
        "model_branches": data.get("model_branches", model_branch_labels(finalize_params(p))),
        "audit_diagnostics": data.get("audit_diagnostics", solver_audit_diagnostics(data, p)),
        "conservation_diagnostics": data.get(
            "conservation_diagnostics", conservation_diagnostics(data, p)
        ),
        "classification": classify_run(data),
        "classification_status": "heuristic_not_evidence",
        "solver_status": {
            "success": bool(data.get("success", False)),
            "message": data.get("message", ""),
            "status": int(data.get("status", -999)),
            "nfev": int(data.get("nfev", -1)),
            "njev": int(data.get("njev", -1)),
            "nlu": int(data.get("nlu", -1)),
            "jac_color_groups": int(data.get("jac_color_groups", -1)),
        },
        "paper_evidence_status": "not_paper_evidence",
        "validation_status": "candidate_not_validated",
    }
    diagnostics_path.write_text(
        dumps_strict_json(diagnostics),
        encoding="utf-8",
    )

    arrays = {
        key: np.asarray(data[key])
        for key in ("x", "t", "J", "W", "u", "theta", "phi", "logJ_raw")
        if key in data
    }
    np.savez_compressed(arrays_path, **arrays)
    return {"params": params_path, "diagnostics": diagnostics_path, "arrays": arrays_path}


def cell_centers(N: int) -> np.ndarray:
    dx = 1.0 / N
    return (np.arange(N) + 0.5) * dx


def phi_from_J(J, p: CanonicalParams, phi_hard_ceil: float | None = None):
    ceiling = p.phi_ceiling if phi_hard_ceil is None else phi_hard_ceil
    J_safe = np.maximum(J, p.phi_p0 / ceiling)
    return p.phi_p0 / J_safe


def harmonic_mean(a, b, eps: float = 1.0e-30):
    return 2.0 * a * b / np.maximum(a + b, eps)


def laplacian_neumann(a, dx):
    out = np.empty_like(a)
    out[1:-1] = (a[2:] - 2 * a[1:-1] + a[:-2]) / dx**2
    out[0] = 2 * (a[1] - a[0]) / dx**2
    out[-1] = 2 * (a[-2] - a[-1]) / dx**2
    return out


def porosity_fields(J, p: CanonicalParams):
    phi = phi_from_J(J, p)
    porosity = np.clip(1.0 - phi, 0.0, 1.0)
    phi_ref = p.phi_p0 / max(p.J_init, p.phi_p0 * 1.02)
    porosity_ref = max(1.0 - phi_ref, 1.0e-12)
    normalized = np.clip(porosity / porosity_ref, 0.0, 1.0)
    return phi, porosity, normalized


def _v1_porosity_closure(norm_porosity, phi, exponent, floor, p: CanonicalParams):
    form = str(p.closure_form).lower()
    if form == "power":
        return floor + (1.0 - floor) * norm_porosity**exponent
    if form == "mackie_meares":
        ratio = np.clip((1.0 - phi) / np.maximum(1.0 + phi, 1.0e-12), 0.0, 1.0)
        phi_ref = p.phi_p0 / max(p.J_init, p.phi_p0 * 1.02)
        ratio_ref = (1.0 - phi_ref) / (1.0 + phi_ref)
        scaled = np.clip(ratio / max(ratio_ref, 1.0e-12), 0.0, 1.0)
        return floor + (1.0 - floor) * scaled**2
    if form == "free_volume":
        raw = np.exp(-p.beta_free_volume * phi / np.maximum(1.0 - phi, 1.0e-12))
        phi_ref = p.phi_p0 / max(p.J_init, p.phi_p0 * 1.02)
        raw_ref = np.exp(-p.beta_free_volume * phi_ref / max(1.0 - phi_ref, 1.0e-12))
        scaled = np.clip(raw / max(raw_ref, 1.0e-300), 0.0, 1.0)
        return floor + (1.0 - floor) * scaled
    raise ValueError(f"unknown closure_form={p.closure_form!r}")


def _canonical_floor(p: CanonicalParams, name: str, legacy_floor: float) -> float:
    if p.floor_scheme == "legacy":
        return legacy_floor
    if name == "accessibility":
        return p.A_min
    if name == "diffusivity":
        return p.D_min
    if name == "mobility":
        return p.M_min
    raise ValueError(name)


def accessibility_factor(J, p: CanonicalParams):
    phi, _, norm_porosity = porosity_fields(J, p)
    if p.transport_closure in {"constant_no_barrier", "accessibility_constant"}:
        return np.ones_like(phi)
    if p.transport_closure in {
        "normalized_porosity_power",
        "transport_constant",
        "diffusivity_constant",
        "mobility_constant",
    }:
        return _v1_porosity_closure(
            norm_porosity,
            phi,
            p.m_act,
            _canonical_floor(p, "accessibility", p.a_floor),
            p,
        )
    return np.maximum(1.0 - phi, 1.0e-12) ** p.m_act + _canonical_floor(
        p, "accessibility", p.a_floor
    )


def mobility_ref(J, theta, p: CanonicalParams):
    phi, _, norm_porosity = porosity_fields(J, p)
    if p.transport_closure in {"constant_no_barrier", "transport_constant", "mobility_constant"}:
        base = np.ones_like(phi)
    elif p.transport_closure in {
        "normalized_porosity_power",
        "accessibility_constant",
        "diffusivity_constant",
    }:
        base = _v1_porosity_closure(
            norm_porosity,
            phi,
            p.m_mob,
            _canonical_floor(p, "mobility", p.mu_floor),
            p,
        )
    else:
        base = np.maximum(1.0 - phi, 1.0e-12) ** p.m_mob + _canonical_floor(
            p, "mobility", p.mu_floor
        )
    return p.M0 * base


def diffusivity_ref(J, theta, p: CanonicalParams):
    phi, _, norm_porosity = porosity_fields(J, p)
    if p.transport_closure in {"constant_no_barrier", "transport_constant", "diffusivity_constant"}:
        base = np.ones_like(phi)
    elif p.transport_closure in {
        "normalized_porosity_power",
        "accessibility_constant",
        "mobility_constant",
    }:
        base = _v1_porosity_closure(
            norm_porosity,
            phi,
            p.m_diff,
            _canonical_floor(p, "diffusivity", p.d_floor),
            p,
        )
    else:
        base = np.maximum(1.0 - phi, 1.0e-12) ** p.m_diff + _canonical_floor(
            p, "diffusivity", p.d_floor
        )
    return p.D0 * base


def conductivity_ref(J, p: CanonicalParams):
    return p.K0 * np.ones_like(J)


def heat_capacity_ref(J, p: CanonicalParams):
    return p.C0 * np.ones_like(J)


def local_chem_pot(J, theta, p: CanonicalParams):
    phi = phi_from_J(J, p)
    chi = p.chi_inf + p.S_chi * theta + p.chi1 * phi
    m_mix = np.log(1 - phi) + phi + chi * phi**2
    if p.chi_closure == "strict_chi_derivative":
        m_mix = m_mix - phi**2 * (1.0 - phi) * p.chi1
    m_el = p.Omega_e * (J - 1.0 / J)
    return m_mix + m_el


def finalize_params(p: CanonicalParams) -> CanonicalParams:
    validate_params(p)
    if p.auto_set_m_b:
        J0 = np.array([p.J_init])
        th0 = np.array([p.theta_init])
        p = replace(p, m_b=float(local_chem_pot(J0, th0, p)[0]))
    return p


def thermal_factor(theta, p: CanonicalParams):
    exp_val = arrhenius_exponent(theta, p)
    if p.use_hill:
        return p.hill_eps + np.maximum(np.exp(exp_val) - 1.0, 0.0)
    return np.exp(exp_val)


def arrhenius_exponent(theta, p: CanonicalParams):
    denom = 1.0 + p.eps_T * np.maximum(theta, -1.0 / p.eps_T * 0.95)
    return np.clip(p.Gamma_A * theta / denom, -p.arrh_exp_cap, p.arrh_exp_cap)


def reaction_rate(u, theta, J, p: CanonicalParams):
    u_eff = np.maximum(u, p.u_floor)
    return u_eff**p.reaction_order * accessibility_factor(J, p) * thermal_factor(theta, p)


def reaction_source_density(J, R, p: CanonicalParams):
    if p.source_scaling == "current_volume":
        return J * R
    if p.source_scaling == "reference_volume":
        return R
    if p.source_scaling == "diagnostic_J_beta":
        return np.maximum(J, 0.0) ** p.source_J_exponent * R
    raise ValueError(f"unknown source_scaling={p.source_scaling!r}")


def state_fluxes(J, W, theta, p: CanonicalParams, dx):
    u = np.maximum(W / J, p.u_floor)

    m_local = local_chem_pot(J, theta, p)
    m = m_local - p.ell**2 * laplacian_neumann(J, dx)

    q = np.zeros(p.N + 1)
    M_cell = mobility_ref(J, theta, p)
    M_face = harmonic_mean(M_cell[:-1], M_cell[1:])
    q[1 : p.N] = -M_face * (m[1:] - m[:-1]) / dx
    q[p.N] = p.Bi_mu * (m[-1] - p.m_b)

    R = reaction_rate(u, theta, J, p)

    nflux = np.zeros(p.N + 1)
    D_cell = diffusivity_ref(J, theta, p)
    D_face = harmonic_mean(D_cell[:-1], D_cell[1:])
    q_int = q[1 : p.N]
    u_up = np.where(q_int >= 0, u[:-1], u[1:])
    nflux[1 : p.N] = q_int * u_up - p.delta * D_face * (u[1:] - u[:-1]) / dx
    nflux[p.N] = p.Bi_c * (u[-1] - 1.0)

    h = np.zeros(p.N + 1)
    K_cell = conductivity_ref(J, p)
    K_face = harmonic_mean(K_cell[:-1], K_cell[1:])
    h[1 : p.N] = -p.alpha * K_face * (theta[1:] - theta[:-1]) / dx
    h[p.N] = p.Bi_T * theta[-1]

    C_cell = heat_capacity_ref(J, p)
    A_cell = accessibility_factor(J, p)
    return {
        "u": u,
        "m_local": m_local,
        "m": m,
        "q": q,
        "R": R,
        "source_density": reaction_source_density(J, R, p),
        "nflux": nflux,
        "h": h,
        "C_ref": C_cell,
        "D_ref": D_cell,
        "K_ref": K_cell,
        "M_ref": M_cell,
        "accessibility": A_cell,
    }


def rhs_mol_logJ(t, y, p: CanonicalParams):
    n = p.N
    dx = 1.0 / n
    bounds = active_numerical_bounds(p)

    logJ = np.clip(y[:n], bounds["logJ_min"], bounds["logJ_max"])
    W = y[n : 2 * n]
    theta = y[2 * n :]

    J = np.exp(logJ)
    aux = state_fluxes(J, W, theta, p, dx)
    source = aux["source_density"]

    q = aux["q"]
    logJ_t = -(q[1:] - q[:-1]) / (dx * J) - p.Bi_J_vol * (
        aux["m_local"] - p.m_b
    ) / J

    nflux = aux["nflux"]
    W_t = (
        -(nflux[1:] - nflux[:-1]) / dx
        - p.Da * source
        + p.B_vol * (J - W)
        + p.Bi_c_vol * (J - W)
    )

    h = aux["h"]
    theta_t = (
        (-(h[1:] - h[:-1]) / dx + p.Da * source) / aux["C_ref"]
        - p.B_Tvol * theta
    )

    return np.concatenate([logJ_t, W_t, theta_t])


def make_jac_sparsity(N: int) -> csc_matrix:
    size = 3 * N
    S = lil_matrix((size, size), dtype=np.float64)
    bw_table = {
        (0, 0): 2,
        (0, 1): -1,
        (0, 2): 1,
        (1, 0): 2,
        (1, 1): 1,
        (1, 2): 1,
        (2, 0): 1,
        (2, 1): 0,
        (2, 2): 1,
    }
    for (kr, kc), w in bw_table.items():
        if w < 0:
            continue
        for i in range(N):
            row = kr * N + i
            for dj in range(-w, w + 1):
                j = i + dj
                if 0 <= j < N:
                    S[row, kc * N + j] = 1.0
    return csc_matrix(S)


def make_sparse_fd_jac(
    rhs_fn,
    S_pattern,
    n3: int,
    atol_h: float = 1.0e-8,
    rtol_h: float = 1.0e-6,
):
    from scipy.optimize._numdiff import group_columns

    S_csc = S_pattern.tocsc()
    indptr = S_csc.indptr.astype(np.int32, copy=True)
    indices = S_csc.indices.astype(np.int32, copy=True)
    nnz = int(S_csc.nnz)

    groups = group_columns(S_pattern)
    n_groups = int(groups.max()) + 1
    cols_in_group = [
        np.where(groups == g)[0].astype(np.int32) for g in range(n_groups)
    ]
    col_rows = [indices[indptr[c] : indptr[c + 1]] for c in range(n3)]

    def jac(t, y):
        f0 = rhs_fn(t, y)
        data = np.zeros(nnz, dtype=np.float64)
        for cols_g in cols_in_group:
            hs = np.maximum(atol_h, rtol_h * np.abs(y[cols_g]))
            yp = y.copy()
            yp[cols_g] += hs
            df = rhs_fn(t, yp) - f0
            for c, h in zip(cols_g, hs):
                rs = col_rows[c]
                data[indptr[c] : indptr[c + 1]] = df[rs] / h
        return csc_matrix((data, indices, indptr), shape=(n3, n3))

    return jac, n_groups


def initial_state(p: CanonicalParams) -> Tuple[np.ndarray, np.ndarray]:
    x = cell_centers(p.N)
    bounds = active_numerical_bounds(p)
    J0 = np.maximum(
        p.J_init + p.eps_J * np.cos(np.pi * x), np.exp(bounds["logJ_min"]) + 1e-6
    )
    u0 = np.maximum(p.u_init + p.eps_u * np.cos(np.pi * x), p.u_floor)
    t0 = p.theta_init + p.eps_theta * x
    logJ0 = np.log(J0)
    W0 = J0 * u0
    return x, np.concatenate([logJ0, W0, t0])


def simulate(
    p: CanonicalParams,
    include_raw_state: bool = False,
    include_audit: bool = True,
) -> Dict[str, Any]:
    p = finalize_params(p)
    x, y0 = initial_state(p)
    n3 = 3 * p.N

    rhs_fn = lambda t, y: rhs_mol_logJ(t, y, p)
    S = make_jac_sparsity(p.N)
    jac_sparse, n_color_groups = make_sparse_fd_jac(rhs_fn, S, n3)

    sol = solve_ivp(
        fun=rhs_fn,
        jac=jac_sparse,
        t_span=(0.0, p.t_end),
        y0=y0,
        t_eval=np.linspace(0, p.t_end, p.n_save),
        method=p.method,
        rtol=p.rtol,
        atol=p.atol,
        max_step=p.max_step,
    )

    if not sol.success:
        raise RuntimeError(sol.message)

    n = p.N
    raw_logJ = sol.y[:n]
    bounds = active_numerical_bounds(p)
    J = np.exp(np.clip(raw_logJ, bounds["logJ_min"], bounds["logJ_max"]))
    W = sol.y[n : 2 * n]
    theta = sol.y[2 * n :]
    u = np.maximum(W / J, p.u_floor)

    data: Dict[str, Any] = {
        "x": x,
        "t": sol.t,
        "J": J,
        "W": W,
        "u": u,
        "theta": theta,
        "phi": phi_from_J(J, p),
        "success": True,
        "message": sol.message,
        "status": int(sol.status),
        "nfev": int(sol.nfev),
        "njev": int(getattr(sol, "njev", -1)),
        "nlu": int(getattr(sol, "nlu", -1)),
        "jac_color_groups": int(n_color_groups),
        "model_branches": model_branch_labels(p),
        "params": params_to_dict(p, finalized=False),
    }
    if include_raw_state or include_audit:
        data["logJ_raw"] = raw_logJ
    if include_audit:
        data["audit_diagnostics"] = solver_audit_diagnostics(data, p)
        data["conservation_diagnostics"] = conservation_diagnostics(data, p)
    return data


def _array_summary(a) -> Dict[str, float]:
    arr = np.asarray(a, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return {"min": float("nan"), "max": float("nan"), "mean": float("nan")}
    return {
        "min": float(np.min(finite)),
        "max": float(np.max(finite)),
        "mean": float(np.mean(finite)),
    }


def solver_audit_diagnostics(data: Dict[str, Any], p: CanonicalParams) -> Dict[str, Any]:
    p = finalize_params(p)
    J = np.asarray(data["J"])
    W = np.asarray(data.get("W", data["J"] * data["u"]))
    theta = np.asarray(data["theta"])
    raw_logJ_available = "logJ_raw" in data
    logJ_raw = np.asarray(data["logJ_raw"]) if raw_logJ_available else np.log(J)
    bounds = active_numerical_bounds(p)

    raw_J = np.exp(np.clip(logJ_raw, -700.0, 700.0))
    with np.errstate(divide="ignore", invalid="ignore"):
        raw_u = W / raw_J
        raw_phi = p.phi_p0 / raw_J

    def _count_fraction(mask):
        mask = np.asarray(mask)
        count = int(np.count_nonzero(mask))
        total = int(mask.size)
        return count, float(count / total) if total else float("nan")

    def _finite_min(a):
        a = np.asarray(a)
        finite = a[np.isfinite(a)]
        return float(np.min(finite)) if finite.size else float("nan")

    def _finite_max(a):
        a = np.asarray(a)
        finite = a[np.isfinite(a)]
        return float(np.max(finite)) if finite.size else float("nan")

    low_count, low_frac = _count_fraction(logJ_raw < bounds["logJ_min"])
    high_count, high_frac = _count_fraction(logJ_raw > bounds["logJ_max"])
    u_clip_count, u_clip_frac = _count_fraction(raw_u < p.u_floor)
    phi_clip_count, phi_clip_frac = _count_fraction(raw_phi > bounds["phi_ceiling"])

    dx = 1.0 / p.N
    nt = J.shape[1] if J.ndim == 2 else 0
    q_surface, n_surface, h_surface = [], [], []
    source_nonfinite = 0
    flux_nonfinite = 0
    coeff_stats = {"accessibility": [], "D_ref": [], "M_ref": []}
    field_stats = {"R": [], "S_R": [], "q": [], "nflux": [], "h": []}
    source_values = []
    arrh_cap_hits = 0
    arrh_total = 0
    for k in range(nt):
        aux = state_fluxes(J[:, k], W[:, k], theta[:, k], p, dx)
        source_density = aux["source_density"]
        source = p.Da * source_density
        source_values.append(source)
        source_nonfinite += int(np.count_nonzero(~np.isfinite(source_density)))
        for name in ("q", "nflux", "h"):
            flux_nonfinite += int(np.count_nonzero(~np.isfinite(aux[name])))
        for name in coeff_stats:
            coeff_stats[name].append(aux[name])
        field_stats["R"].append(aux["R"])
        field_stats["S_R"].append(source_density)
        field_stats["q"].append(aux["q"])
        field_stats["nflux"].append(aux["nflux"])
        field_stats["h"].append(aux["h"])
        q_surface.append(aux["q"][-1])
        n_surface.append(aux["nflux"][-1])
        h_surface.append(aux["h"][-1])
        denom = 1.0 + p.eps_T * np.maximum(theta[:, k], -1.0 / p.eps_T * 0.95)
        raw_exp = p.Gamma_A * theta[:, k] / denom
        arrh_cap_hits += int(np.count_nonzero(np.abs(raw_exp) >= p.arrh_exp_cap))
        arrh_total += int(raw_exp.size)

    diagnostics = {
        "model_branches": model_branch_labels(p),
        "active_numerical_bounds": bounds,
        "raw_logJ_available": bool(raw_logJ_available),
        "min_raw_logJ": _finite_min(logJ_raw),
        "max_raw_logJ": _finite_max(logJ_raw),
        "logJ_low_clip_count": low_count,
        "logJ_low_clip_fraction": low_frac,
        "logJ_high_clip_count": high_count,
        "logJ_high_clip_fraction": high_frac,
        "min_W": _finite_min(W),
        "min_raw_u": _finite_min(raw_u),
        "u_floor_clip_count": u_clip_count,
        "u_floor_clip_fraction": u_clip_frac,
        "max_phi_before_clip": _finite_max(raw_phi),
        "phi_hard_ceiling": bounds["phi_ceiling"],
        "phi_hard_ceiling_exceed_count": phi_clip_count,
        "phi_hard_ceiling_exceed_fraction": phi_clip_frac,
        "arrh_exp_cap_hit_count": int(arrh_cap_hits),
        "arrh_exp_cap_hit_fraction": float(arrh_cap_hits / arrh_total)
        if arrh_total
        else float("nan"),
        "nonfinite_J_count": int(np.count_nonzero(~np.isfinite(J))),
        "nonfinite_W_count": int(np.count_nonzero(~np.isfinite(W))),
        "nonfinite_u_count": int(np.count_nonzero(~np.isfinite(raw_u))),
        "nonfinite_theta_count": int(np.count_nonzero(~np.isfinite(theta))),
        "nonfinite_source_count": int(source_nonfinite),
        "nonfinite_flux_count": int(flux_nonfinite),
        "surface_q": _array_summary(q_surface),
        "surface_nflux": _array_summary(n_surface),
        "surface_h": _array_summary(h_surface),
        "source": _array_summary(np.concatenate(source_values) if source_values else []),
        "accessibility": _array_summary(np.concatenate(coeff_stats["accessibility"]) if nt else []),
        "D_ref": _array_summary(np.concatenate(coeff_stats["D_ref"]) if nt else []),
        "M_ref": _array_summary(np.concatenate(coeff_stats["M_ref"]) if nt else []),
        "A": _array_summary(np.concatenate(coeff_stats["accessibility"]) if nt else []),
        "D": _array_summary(np.concatenate(coeff_stats["D_ref"]) if nt else []),
        "M": _array_summary(np.concatenate(coeff_stats["M_ref"]) if nt else []),
        "R": _array_summary(np.concatenate(field_stats["R"]) if nt else []),
        "S_R": _array_summary(np.concatenate(field_stats["S_R"]) if nt else []),
        "q": _array_summary(np.concatenate(field_stats["q"]) if nt else []),
        "n": _array_summary(np.concatenate(field_stats["nflux"]) if nt else []),
        "h": _array_summary(np.concatenate(field_stats["h"]) if nt else []),
        "params": params_to_dict(p, finalized=False),
    }
    return diagnostics


def conservation_diagnostics(
    data: Dict[str, Any], p: CanonicalParams, late_frac: float = 0.60
) -> Dict[str, Any]:
    p = finalize_params(p)
    t = np.asarray(data["t"])
    J = np.asarray(data["J"])
    W = np.asarray(data.get("W", data["J"] * data["u"]))
    theta = np.asarray(data["theta"])
    dx = 1.0 / p.N
    nt = len(t)

    reactant_inventory = np.sum(W, axis=0) * dx
    heat_inventory = np.zeros(nt)
    reactant_rhs = np.zeros(nt)
    heat_rhs = np.zeros(nt)
    enthalpy_adv_ratio = np.zeros(nt)

    for k in range(nt):
        aux = state_fluxes(J[:, k], W[:, k], theta[:, k], p, dx)
        source = p.Da * aux["source_density"]
        reactant_rhs[k] = -(aux["nflux"][-1] - aux["nflux"][0]) - np.sum(source) * dx
        reactant_rhs[k] += np.sum((p.B_vol + p.Bi_c_vol) * (J[:, k] - W[:, k])) * dx

        heat_inventory[k] = np.sum(aux["C_ref"] * theta[:, k]) * dx
        heat_rhs[k] = -(aux["h"][-1] - aux["h"][0]) + np.sum(source) * dx
        heat_rhs[k] += np.sum(-aux["C_ref"] * p.B_Tvol * theta[:, k]) * dx

        if p.Pe_T != 0.0:
            enthalpy_face = np.zeros(p.N + 1)
            temp_like = p.Theta_infty + theta[:, k]
            if p.N > 1:
                temp_face = 0.5 * (temp_like[:-1] + temp_like[1:])
                enthalpy_face[1 : p.N] = -p.alpha * p.Pe_T * temp_face * aux["q"][1 : p.N]
            enthalpy_face[p.N] = -p.alpha * p.Pe_T * temp_like[-1] * aux["q"][p.N]
            enthalpy_scale = max(abs(aux["h"][-1] - aux["h"][0]), 1.0e-30)
            enthalpy_adv_ratio[k] = abs(enthalpy_face[-1] - enthalpy_face[0]) / enthalpy_scale

    def _integrated_residual(inventory, rhs, sl):
        if len(t[sl]) < 2:
            return float("nan")
        inv = inventory[sl]
        rhs_w = rhs[sl]
        tt = t[sl]
        dt = np.diff(tt)
        step_res = np.diff(inv) - 0.5 * (rhs_w[:-1] + rhs_w[1:]) * dt
        scale = max(
            float(np.max(np.abs(inv))),
            float(np.sum(0.5 * (np.abs(rhs_w[:-1]) + np.abs(rhs_w[1:])) * dt)),
            1.0e-12,
        )
        return float(np.sqrt(np.mean(step_res**2)) / scale)

    all_sl = slice(0, nt)
    late_sl = tail_slice(nt, late_frac)
    return {
        "model_branches": model_branch_labels(p),
        "reactant_balance_residual": _integrated_residual(
            reactant_inventory, reactant_rhs, all_sl
        ),
        "heat_balance_residual": _integrated_residual(heat_inventory, heat_rhs, all_sl),
        "reactant_balance_residual_late": _integrated_residual(
            reactant_inventory, reactant_rhs, late_sl
        ),
        "heat_balance_residual_late": _integrated_residual(
            heat_inventory, heat_rhs, late_sl
        ),
        "max_enthalpy_advection_to_conduction_ratio": float(
            np.nanmax(enthalpy_adv_ratio)
        )
        if nt
        else float("nan"),
        "reactant_inventory_initial": float(reactant_inventory[0]),
        "reactant_inventory_final": float(reactant_inventory[-1]),
        "heat_inventory_initial": float(heat_inventory[0]),
        "heat_inventory_final": float(heat_inventory[-1]),
    }


def tail_slice(n_t, frac0=0.60):
    return slice(max(0, int(frac0 * n_t)), n_t)


def detrend(t, y):
    c = np.polyfit(t, y, 1)
    return y - np.polyval(c, t)


def oscillation_metrics(t, y, frac0=0.60, amp_floor=1.0e-3):
    sl = tail_slice(len(t), frac0)
    tt, yy = t[sl], y[sl]
    if len(tt) < 20:
        return {"amp": 0.0, "period": np.nan, "n_peaks": 0, "oscillatory": False}
    yd = detrend(tt, yy)
    amp = float(np.max(yd) - np.min(yd))
    prom = max(0.15 * amp, amp_floor)
    mdist = max(3, len(yd) // 20)
    peaks, _ = find_peaks(yd, prominence=prom, distance=mdist)
    troughs, _ = find_peaks(-yd, prominence=prom, distance=mdist)
    period = np.nan
    peak_cv = np.nan
    if len(peaks) >= 2:
        dT = np.diff(tt[peaks])
        period = float(np.mean(dT))
        peak_cv = float(np.std(dT) / np.mean(dT)) if len(dT) >= 2 else 0.0
    osc = (
        amp > amp_floor
        and len(peaks) >= 2
        and len(troughs) >= 2
        and (np.isnan(peak_cv) or peak_cv < 0.40)
    )
    return {"amp": amp, "period": period, "n_peaks": int(len(peaks)), "oscillatory": osc}


def classify_run(data: Dict[str, Any]) -> Dict[str, Any]:
    J, u, theta = data["J"], data["u"], data["theta"]
    t = data["t"]
    J_mean = np.mean(J, axis=0)
    theta_mean = np.mean(theta, axis=0)
    J_std = np.std(J, axis=0)
    theta_std = np.std(theta, axis=0)

    th_m = oscillation_metrics(t, theta_mean, amp_floor=2.0e-3)
    J_m = oscillation_metrics(t, J_mean, amp_floor=2.0e-4)

    osc = bool(th_m["oscillatory"] or J_m["oscillatory"])
    sl = tail_slice(len(t))
    non_uni = max(np.mean(J_std[sl]), np.mean(theta_std[sl])) > 2.0e-3

    theta_f = float(theta_mean[-1])
    ts = "hot" if theta_f > 0.25 else ("cold" if theta_f < 0.05 else "warm")

    if osc and non_uni:
        label = "oscillatory_nonuniform"
    elif osc:
        label = "oscillatory_uniform"
    elif non_uni:
        label = f"steady_{ts}_nonuniform"
    else:
        label = f"steady_{ts}_uniform"

    def _f(x):
        return float(x) if np.isfinite(x) else float("nan")

    return {
        "label": label,
        "is_oscillatory": int(osc),
        "is_nonuniform": int(non_uni),
        "thermal_state": ts,
        "theta_amp": _f(th_m["amp"]),
        "J_amp": _f(J_m["amp"]),
        "theta_period": _f(th_m["period"] or float("nan")),
        "J_period": _f(J_m["period"] or float("nan")),
        "theta_peaks": th_m["n_peaks"],
        "J_peaks": J_m["n_peaks"],
        "J_mean_final": _f(J_mean[-1]),
        "theta_mean_final": theta_f,
        "u_mean_final": _f(np.mean(u, axis=0)[-1]),
        "nfev": data.get("nfev", -1),
    }
