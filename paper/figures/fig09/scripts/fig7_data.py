"""
fig7_data.py — Shared simulation cache for the spinodal-decomposition
appendix figure.

Runs the pure-Cahn-Hilliard simulation from `spinodal_demo.run_spinodal`
once and caches the (x, t, J) field plus the analytic
{f_J, k*, lambda*, sigma*} info to ``data/fig7/raw_simulation.npz``.

Cache parameters mirror the original `spinodal_demo` defaults so the
appendix matches the analytic predictions reported in the text:
N=301, ell=0.01, J0=0.30, theta=1.5, perturbation=0.001, t_end=0.5,
seed=42.
"""
import os, sys
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig7"))
RAW = os.path.join(DATA_DIR, "raw_simulation.npz")

SIM_PARAMS = dict(N=301, ell=0.01, J0=0.30, theta0=1.5,
                  perturbation=0.001, t_end=0.5, seed=42)


def load_or_compute():
    """Return (x, t, J, info) from cache, computing if needed."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(RAW):
        z = np.load(RAW, allow_pickle=True)
        return dict(
            x=z["x"], t=z["t"], J=z["J"],
            theta0=float(z["theta0"]),
            J0=float(z["J0"]),
            f_J=float(z["f_J"]),
            k_star=float(z["k_star"]),
            lambda_star=float(z["lambda_star"]),
            sigma_star=float(z["sigma_star"]),
            ell=float(z["ell"]),
            N=int(z["N"]),
        )

    from spinodal_demo import run_spinodal
    result = run_spinodal(**SIM_PARAMS)
    if result is None:
        raise RuntimeError("spinodal simulation failed")
    info = result["info"]
    np.savez(RAW,
             x=result["x"], t=result["t"], J=result["J"],
             theta0=np.float64(result["theta0"]),
             J0=np.float64(result["J0"]),
             f_J=np.float64(info["f_J"]),
             k_star=np.float64(info.get("k_star", np.nan)),
             lambda_star=np.float64(info.get("lambda_star", np.nan)),
             sigma_star=np.float64(info.get("sigma_star", np.nan)),
             ell=np.float64(SIM_PARAMS["ell"]),
             N=np.int64(SIM_PARAMS["N"]))
    print(f"  Saved raw cache: {RAW}")
    return load_or_compute()
