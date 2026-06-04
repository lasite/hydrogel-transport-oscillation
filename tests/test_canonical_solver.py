import numpy as np
import pytest

from paper.solver.paper_latest_cpu.scan_optimized import (
    Params as LegacyParams,
    simulate as legacy_simulate,
)
from paper.solver.canonical_cpu.solver import (
    CanonicalParams,
    accessibility_factor,
    conservation_diagnostics,
    diffusivity_ref,
    finalize_params,
    initial_state,
    local_chem_pot,
    make_jac_sparsity,
    mobility_ref,
    params_to_dict,
    reaction_source_density,
    rhs_mol_logJ,
    save_run_bundle,
    simulate,
    state_fluxes,
)
from paper.solver.canonical_cpu.run_smoke_checks import (
    _cleanup_stale_outputs,
    _expected_output_names,
    _suite_metadata,
)


def _uniform_state(p: CanonicalParams, J: float, u: float, theta: float) -> np.ndarray:
    logJ = np.full(p.N, np.log(J), dtype=float)
    W = np.full(p.N, J * u, dtype=float)
    th = np.full(p.N, theta, dtype=float)
    return np.concatenate([logJ, W, th])


def test_final_canonical_defaults_use_reference_source_effective_chi_and_normalized_transport():
    p = CanonicalParams()
    metadata = params_to_dict(p)

    assert p.source_scaling == "reference_volume"
    assert p.chi_closure == "effective_osmotic_chi"
    assert p.transport_closure == "normalized_porosity_power"
    assert p.floor_scheme == "canonical_consistent"
    assert p.boundary_scheme == "cell_center_robin"
    assert p.enthalpy_advection is False
    assert metadata["model_branches"]["source_scaling"] == "reference_volume"
    assert metadata["model_branches"]["chi_closure"] == "effective_osmotic_chi"
    assert metadata["model_branches"]["transport_closure"] == "normalized_porosity_power"
    assert metadata["model_branches"]["floor_scheme"] == "canonical_consistent"


def test_reaction_off_closed_reactant_inventory_is_conserved_by_rhs():
    p = finalize_params(
        CanonicalParams(
            N=9,
            Da=0.0,
            Bi_c=0.0,
            B_vol=0.0,
            Bi_c_vol=0.0,
            eps_u=0.0,
            eps_J=0.0,
            eps_theta=0.0,
        )
    )
    y = _uniform_state(p, J=1.27, u=0.43, theta=0.02)
    dydt = rhs_mol_logJ(0.0, y, p)
    W_t = dydt[p.N : 2 * p.N]

    assert abs(float(np.sum(W_t) / p.N)) < 1.0e-12


def test_reaction_off_closed_heat_inventory_is_conserved_by_rhs():
    p = finalize_params(
        CanonicalParams(
            N=9,
            Da=0.0,
            Bi_T=0.0,
            B_Tvol=0.0,
            eps_u=0.0,
            eps_J=0.0,
            eps_theta=0.0,
        )
    )
    y = _uniform_state(p, J=1.21, u=0.51, theta=0.13)
    dydt = rhs_mol_logJ(0.0, y, p)
    theta_t = dydt[2 * p.N :]

    assert abs(float(np.sum(theta_t) / p.N)) < 1.0e-12


def test_nonuniform_closed_domain_conserves_reactant_and_heat_when_reaction_off():
    p = finalize_params(
        CanonicalParams(
            N=9,
            Da=0.0,
            Bi_mu=0.0,
            Bi_c=0.0,
            Bi_T=0.0,
            B_vol=0.0,
            B_Tvol=0.0,
            Bi_c_vol=0.0,
            Bi_J_vol=0.0,
        )
    )
    x = np.linspace(0.0, 1.0, p.N)
    J = 1.2 + 0.04 * np.cos(np.pi * x)
    u = 0.45 + 0.03 * np.sin(np.pi * x)
    theta = 0.1 + 0.02 * np.cos(2.0 * np.pi * x)
    y = np.concatenate([np.log(J), J * u, theta])
    dydt = rhs_mol_logJ(0.0, y, p)

    assert abs(float(np.sum(dydt[p.N : 2 * p.N]) / p.N)) < 1.0e-12
    assert abs(float(np.sum(dydt[2 * p.N :]) / p.N)) < 1.0e-12


def test_closed_domain_conserves_swelling_inventory_when_solvent_exchange_is_off():
    p = finalize_params(
        CanonicalParams(
            N=11,
            Da=0.0,
            Bi_mu=0.0,
            Bi_c=0.0,
            Bi_T=0.0,
            B_vol=0.0,
            B_Tvol=0.0,
            Bi_c_vol=0.0,
            Bi_J_vol=0.0,
        )
    )
    x = np.linspace(0.0, 1.0, p.N)
    J = 1.22 + 0.04 * np.cos(np.pi * x)
    u = 0.48 + 0.02 * np.sin(np.pi * x)
    theta = 0.06 + 0.01 * np.cos(2.0 * np.pi * x)
    y = np.concatenate([np.log(J), J * u, theta])
    dydt = rhs_mol_logJ(0.0, y, p)
    J_t = J * dydt[: p.N]

    assert abs(float(np.sum(J_t) / p.N)) < 1.0e-12


def test_closed_domain_reaction_source_transfers_reactant_to_heat_inventory():
    p = finalize_params(
        CanonicalParams(
            N=9,
            Da=2.0,
            Bi_mu=0.0,
            Bi_c=0.0,
            Bi_T=0.0,
            B_vol=0.0,
            B_Tvol=0.0,
            Bi_c_vol=0.0,
            Bi_J_vol=0.0,
        )
    )
    x = np.linspace(0.0, 1.0, p.N)
    J = 1.25 + 0.03 * np.cos(np.pi * x)
    u = 0.55 + 0.02 * np.sin(np.pi * x)
    theta = 0.08 + 0.01 * x
    y = np.concatenate([np.log(J), J * u, theta])
    dydt = rhs_mol_logJ(0.0, y, p)
    W_t = dydt[p.N : 2 * p.N]
    theta_t = dydt[2 * p.N :]

    aux = state_fluxes(J, J * u, theta, p, dx=1.0 / p.N)
    source = reaction_source_density(J, aux["R"], p)

    assert p.source_scaling == "reference_volume"
    np.testing.assert_allclose(source, aux["R"])
    assert abs(float(np.sum(W_t + theta_t) / p.N)) < 1.0e-12


def test_surface_reactant_flux_sign_supplies_bath_reactant_when_u_below_one():
    p = finalize_params(CanonicalParams(N=7, Da=0.0, Bi_c=0.7, Bi_T=0.0))
    y = _uniform_state(p, J=1.3, u=0.4, theta=0.0)
    J = np.exp(y[: p.N])
    W = y[p.N : 2 * p.N]
    theta = y[2 * p.N :]
    aux = state_fluxes(J, W, theta, p, dx=1.0 / p.N)
    dydt = rhs_mol_logJ(0.0, y, p)
    W_t = dydt[p.N : 2 * p.N]

    assert aux["nflux"][-1] < 0.0
    assert float(np.sum(W_t) / p.N) > 0.0


def test_no_lcst_coupling_removes_temperature_dependence_from_local_potential():
    p = finalize_params(CanonicalParams(N=5, S_chi=0.0, auto_set_m_b=False))
    J = np.array([1.1, 1.3, 1.6])
    cold = local_chem_pot(J, np.zeros_like(J), p)
    hot = local_chem_pot(J, np.full_like(J, 2.0), p)

    np.testing.assert_allclose(cold, hot, rtol=0.0, atol=1.0e-14)


def test_no_barrier_transport_branch_sets_accessibility_diffusivity_mobility_to_one():
    p = finalize_params(CanonicalParams(N=5, transport_closure="constant_no_barrier"))
    y = _uniform_state(p, J=1.4, u=0.8, theta=0.1)
    J = np.exp(y[: p.N])
    W = y[p.N : 2 * p.N]
    theta = y[2 * p.N :]
    aux = state_fluxes(J, W, theta, p, dx=1.0 / p.N)

    np.testing.assert_allclose(aux["accessibility"], 1.0)
    np.testing.assert_allclose(aux["D_ref"], p.D0)
    np.testing.assert_allclose(aux["M_ref"], p.M0)


def test_source_scaling_branch_changes_source_density_only_not_fluxes():
    y_params = dict(
        N=6,
        J_init=1.35,
        u_init=0.62,
        theta_init=0.2,
        eps_J=0.0,
        eps_u=0.0,
        eps_theta=0.0,
        source_scaling="current_volume",
    )
    p_current = finalize_params(CanonicalParams(**y_params))
    p_reference = finalize_params(
        CanonicalParams(**{**y_params, "source_scaling": "reference_volume"})
    )
    _, y = initial_state(p_current)
    J = np.exp(y[: p_current.N])
    W = y[p_current.N : 2 * p_current.N]
    theta = y[2 * p_current.N :]

    aux_current = state_fluxes(J, W, theta, p_current, dx=1.0 / p_current.N)
    aux_reference = state_fluxes(J, W, theta, p_reference, dx=1.0 / p_reference.N)
    source_current = reaction_source_density(J, aux_current["R"], p_current)
    source_reference = reaction_source_density(J, aux_reference["R"], p_reference)

    for key in ("q", "nflux", "h"):
        np.testing.assert_allclose(aux_current[key], aux_reference[key])
    np.testing.assert_allclose(source_current, J * source_reference)


def test_diagnostic_accessibility_constant_branch_only_removes_reaction_accessibility_barrier():
    p = finalize_params(
        CanonicalParams(
            N=5,
            transport_closure="accessibility_constant",
            J_init=1.3,
            m_act=8.0,
            m_diff=3.0,
            m_mob=2.0,
        )
    )
    y = _uniform_state(p, J=0.45, u=0.8, theta=0.1)
    J = np.exp(y[: p.N])
    W = y[p.N : 2 * p.N]
    theta = y[2 * p.N :]
    aux = state_fluxes(J, W, theta, p, dx=1.0 / p.N)

    np.testing.assert_allclose(aux["accessibility"], 1.0)
    assert float(np.max(aux["D_ref"])) < p.D0
    assert float(np.max(aux["M_ref"])) < p.M0


def test_diagnostic_transport_constant_branch_only_removes_diffusivity_and_mobility_barriers():
    p = finalize_params(
        CanonicalParams(
            N=5,
            transport_closure="transport_constant",
            J_init=1.3,
            m_act=8.0,
            m_diff=3.0,
            m_mob=2.0,
        )
    )
    y = _uniform_state(p, J=0.45, u=0.8, theta=0.1)
    J = np.exp(y[: p.N])
    W = y[p.N : 2 * p.N]
    theta = y[2 * p.N :]
    aux = state_fluxes(J, W, theta, p, dx=1.0 / p.N)

    assert float(np.max(aux["accessibility"])) < 1.0
    np.testing.assert_allclose(aux["D_ref"], p.D0)
    np.testing.assert_allclose(aux["M_ref"], p.M0)


def test_diagnostic_J_beta_source_scaling_interpolates_reference_and_current_volume_sources():
    p = finalize_params(
        CanonicalParams(
            N=6,
            source_scaling="diagnostic_J_beta",
            source_J_exponent=0.5,
        )
    )
    _, y = initial_state(p)
    J = np.exp(y[: p.N])
    W = y[p.N : 2 * p.N]
    theta = y[2 * p.N :]
    aux = state_fluxes(J, W, theta, p, dx=1.0 / p.N)
    source = reaction_source_density(J, aux["R"], p)

    np.testing.assert_allclose(source, np.sqrt(J) * aux["R"])


def test_normalized_porosity_power_uses_consistent_minimum_floors_for_A_D_M():
    p = finalize_params(
        CanonicalParams(
            N=5,
            transport_closure="normalized_porosity_power",
            floor_scheme="canonical_consistent",
            A_min=0.12,
            D_min=0.23,
            M_min=0.34,
            D0=2.5,
            M0=1.7,
        )
    )
    J = np.array([0.24, 0.5, 1.3, 2.0])
    theta = np.zeros_like(J)

    A = accessibility_factor(J, p)
    D = diffusivity_ref(J, theta, p)
    M = mobility_ref(J, theta, p)

    assert np.min(A) >= p.A_min
    assert np.max(A) <= 1.0
    assert np.min(D) >= p.D0 * p.D_min
    assert np.max(D) <= p.D0
    assert np.min(M) >= p.M0 * p.M_min
    assert np.max(M) <= p.M0


@pytest.mark.filterwarnings("ignore:.*invalid value encountered.*")
def test_canonical_legacy_branch_reproduces_short_legacy_default_trajectory():
    kwargs = dict(N=8, t_end=0.2, n_save=5, max_step=0.05, rtol=1.0e-6, atol=1.0e-8)
    legacy_data = legacy_simulate(LegacyParams(**kwargs))
    canonical_data = simulate(
        CanonicalParams(
            **kwargs,
            source_scaling="current_volume",
            chi_closure="effective_osmotic_chi",
            transport_closure="legacy_porosity_power",
            floor_scheme="legacy",
            boundary_scheme="cell_center_robin",
            enthalpy_advection=False,
        )
    )

    for key in ("J", "W", "u", "theta"):
        np.testing.assert_allclose(canonical_data[key], legacy_data[key], rtol=2.0e-9, atol=2.0e-10)


def test_conservation_diagnostics_report_branch_labels_and_inventory_residuals():
    p = CanonicalParams(N=8, t_end=0.2, n_save=5, max_step=0.05, Da=0.0)
    data = simulate(p, include_audit=True)
    diagnostics = conservation_diagnostics(data, p)

    assert diagnostics["model_branches"]["source_scaling"] == "reference_volume"
    assert "reactant_balance_residual" in diagnostics
    assert "heat_balance_residual" in diagnostics


def test_clipping_bounds_are_controlled_by_saved_params():
    p = finalize_params(
        CanonicalParams(
            N=4,
            J_min=0.25,
            J_max=1.1,
            phi_ceiling=0.7,
            Da=0.0,
        )
    )
    y = _uniform_state(p, J=1.5, u=0.5, theta=0.0)
    data = {
        "t": np.array([0.0]),
        "J": np.full((p.N, 1), 1.1),
        "W": np.full((p.N, 1), 0.55),
        "u": np.full((p.N, 1), 0.5),
        "theta": np.zeros((p.N, 1)),
        "logJ_raw": y[: p.N, None],
    }
    diagnostics = simulate(
        CanonicalParams(N=4, J_min=0.25, J_max=1.1, phi_ceiling=0.7, t_end=0.01, n_save=2),
        include_audit=True,
    )["audit_diagnostics"]

    assert diagnostics["active_numerical_bounds"]["J_min"] == 0.25
    assert diagnostics["active_numerical_bounds"]["J_max"] == 1.1
    assert diagnostics["active_numerical_bounds"]["phi_ceiling"] == 0.7
    assert data["J"].shape == (p.N, 1)


def test_strict_chi_derivative_branch_changes_local_potential_and_label():
    p_effective = finalize_params(CanonicalParams(N=5, chi_closure="effective_osmotic_chi"))
    p_strict = finalize_params(CanonicalParams(N=5, chi_closure="strict_chi_derivative"))
    J = np.array([1.1, 1.3, 1.6])
    theta = np.full_like(J, 0.2)

    effective = local_chem_pot(J, theta, p_effective)
    strict = local_chem_pot(J, theta, p_strict)

    assert p_strict.chi_closure == "strict_chi_derivative"
    assert np.max(np.abs(effective - strict)) > 0.0


def test_sparse_jacobian_pattern_covers_finite_difference_couplings():
    p = finalize_params(CanonicalParams(N=5, t_end=0.1, n_save=3))
    _, y = initial_state(p)
    y = y + np.linspace(0.0, 1.0e-4, y.size)
    f0 = rhs_mol_logJ(0.0, y, p)
    pattern = make_jac_sparsity(p.N).toarray().astype(bool)
    dense_nonzero = np.zeros_like(pattern)
    for col in range(y.size):
        h = max(1.0e-8, 1.0e-6 * abs(y[col]))
        yp = y.copy()
        yp[col] += h
        df = (rhs_mol_logJ(0.0, yp, p) - f0) / h
        dense_nonzero[:, col] = np.abs(df) > 1.0e-8

    assert not np.any(dense_nonzero & ~pattern)


def test_save_run_bundle_persists_params_diagnostics_and_arrays(tmp_path):
    p = CanonicalParams(N=6, t_end=0.1, n_save=4, max_step=0.05)
    data = simulate(p, include_audit=True)

    written = save_run_bundle(data, p, tmp_path, run_name="unit_smoke")

    assert written["params"].exists()
    assert written["diagnostics"].exists()
    assert written["arrays"].exists()
    params_text = written["params"].read_text(encoding="utf-8")
    diagnostics_text = written["diagnostics"].read_text(encoding="utf-8")
    assert '"source_scaling": "reference_volume"' in params_text
    assert '"logJ_low_clip_count"' in diagnostics_text
    assert '"classification_status": "heuristic_not_evidence"' in diagnostics_text


def test_smoke_cleanup_keeps_expected_outputs_and_removes_stale_files(tmp_path):
    expected = _expected_output_names(["grid_N15", "control_no_reaction"])
    keep = tmp_path / "grid_N15_params.json"
    stale = tmp_path / "old_case_params.json"
    ignored = tmp_path / "notes.txt"
    keep.write_text("old expected output", encoding="utf-8")
    stale.write_text("stale output", encoding="utf-8")
    ignored.write_text("not managed by smoke runner", encoding="utf-8")

    removed = _cleanup_stale_outputs(tmp_path, expected)

    assert keep.exists()
    assert ignored.exists()
    assert not stale.exists()
    assert removed == ["old_case_params.json"]


def test_smoke_suite_metadata_records_command_and_source_hashes():
    metadata = _suite_metadata("results/solver_smoke")

    assert metadata["command"] == "python -m paper.solver.canonical_cpu.run_smoke_checks"
    assert metadata["outdir"] == "results/solver_smoke"
    assert metadata["source_file_sha256"]["paper/solver/canonical_cpu/solver.py"]
    assert metadata["source_file_sha256"]["paper/solver/canonical_cpu/run_smoke_checks.py"]
    assert metadata["git"]["branch"]


def test_canonical_nominal_run_reports_no_clipping_and_full_audit_summaries():
    p = CanonicalParams(N=9, t_end=0.1, n_save=4, max_step=0.05, Da=0.0)
    data = simulate(p, include_audit=True)
    audit = data["audit_diagnostics"]

    assert audit["logJ_low_clip_count"] == 0
    assert audit["logJ_high_clip_count"] == 0
    assert audit["u_floor_clip_count"] == 0
    assert audit["phi_hard_ceiling_exceed_count"] == 0
    assert audit["arrh_exp_cap_hit_count"] == 0
    assert audit["nonfinite_source_count"] == 0
    assert audit["nonfinite_flux_count"] == 0
    for key in ("A", "D", "M", "R", "S_R", "q", "n", "h"):
        assert set(audit[key]) == {"min", "max", "mean"}
