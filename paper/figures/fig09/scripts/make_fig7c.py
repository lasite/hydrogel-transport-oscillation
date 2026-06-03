"""
make_fig7c.py — Panel (c): spectral growth at k ≈ k* with the
analytic exp(2 sigma* tau) reference line.

Cache: data/fig7/panel_c.npz
Render: Figure/fig7/panel_c.{pdf,png}
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig7_style import (
    set_style, new_panel_fig, save_panel, add_panel_label,
)
from fig7_data import load_or_compute

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig7"))
CACHE = os.path.join(DATA_DIR, "panel_c.npz")


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    d = load_or_compute()
    x = d["x"]; t = d["t"]; J = d["J"]
    Nx = len(x)
    k_arr = np.fft.rfftfreq(Nx, d=1.0 / Nx) * 2 * np.pi
    kstar = float(d["k_star"])
    band = (k_arr >= 0.7 * kstar) & (k_arr <= 1.3 * kstar)

    amp = np.zeros(len(t))
    for i in range(len(t)):
        Jc = J[:, i] - J[:, i].mean()
        spec = np.abs(np.fft.rfft(Jc)) ** 2
        amp[i] = float(spec[band].mean()) if band.any() else 0.0
    amp = np.maximum(amp, 1e-300)

    np.savez(CACHE,
             t=t, amp=amp,
             k_star=np.float64(kstar),
             sigma_star=np.float64(d["sigma_star"]))
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax = new_panel_fig()

    t = d["t"]; amp = d["amp"]
    sigma = float(d["sigma_star"])

    ax.semilogy(t, amp, "-", color="#1f77b4", lw=1.0, label=r"sim")

    # Anchor analytic exp(2 sigma* tau) at the first time amp climbs
    # 3x above the early-time floor.
    floor = amp[: max(1, len(t) // 100)].mean()
    rising = np.where(amp > 3 * floor)[0]
    i_anchor = int(rising[0]) if rising.size > 0 else max(1, len(t) // 20)
    t_anchor = t[i_anchor]
    a_anchor = amp[i_anchor]
    sat = amp.max()
    if sigma > 0 and a_anchor > 0:
        t_line_end = t_anchor + np.log(3 * sat / a_anchor) / (2 * sigma)
    else:
        t_line_end = t[-1]
    mask = (t >= t_anchor) & (t <= min(t_line_end, t[-1]))
    if mask.sum() >= 2:
        t_line = t[mask]
        amp_line = a_anchor * np.exp(2 * sigma * (t_line - t_anchor))
        ax.semilogy(t_line, amp_line, "--", color="#d62728", lw=1.0,
                    label=rf"$\exp(2\sigma^* \tau)$, $\sigma^*={sigma:.0f}$")

    y_lo = max(amp[amp > 0].min() / 10.0, 1e-12)
    y_hi = amp.max() * 10.0
    ax.set_ylim(y_lo, y_hi)
    if sigma > 0:
        t_zoom = min(11.0 / sigma, t[-1])
    else:
        t_zoom = t[-1]
    ax.set_xlim(0, t_zoom)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$\langle |\hat J(k)|^2\rangle_{[0.7,1.3]\,k^*}$")
    ax.tick_params(direction="out", length=2.2)
    ax.legend(loc="lower right", framealpha=0.92, handlelength=1.4,
              borderpad=0.30, labelspacing=0.30, handletextpad=0.5)

    add_panel_label(ax, "c")
    save_panel(fig, "panel_c")


if __name__ == "__main__":
    render()
