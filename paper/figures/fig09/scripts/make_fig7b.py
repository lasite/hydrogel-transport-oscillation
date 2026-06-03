"""
make_fig7b.py — Panel (b): J(x) spatial profiles at selected times.

Cache: data/fig7/panel_b.npz
Render: Figure/fig7/panel_b.{pdf,png}
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig7_style import (
    set_style, new_panel_fig, save_panel, add_panel_label,
)
from fig7_data import load_or_compute

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig7"))
CACHE = os.path.join(DATA_DIR, "panel_b.npz")
N_PROFILES = 6


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    d = load_or_compute()
    t_idx = np.linspace(0, len(d["t"]) - 1, N_PROFILES).astype(int)
    np.savez(CACHE,
             x=d["x"], t=d["t"][t_idx], J=d["J"][:, t_idx],
             J0=np.float64(d["J0"]))
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax = new_panel_fig()

    x = d["x"]; t = d["t"]; J = d["J"]
    colors = plt.cm.viridis(np.linspace(0, 1, len(t)))
    for i, c in enumerate(colors):
        ax.plot(x, J[:, i], color=c, lw=0.8,
                label=rf"$\tau={t[i]:.3f}$")
    ax.axhline(float(d["J0"]), color="k", ls=":", lw=0.5, alpha=0.5)

    ax.set_xlabel(r"$x/H_0$")
    ax.set_ylabel(r"$J(x)$")
    ax.tick_params(direction="out", length=2.2)
    ax.legend(loc="upper right", framealpha=0.85, ncol=2,
              handlelength=1.0, borderpad=0.30, labelspacing=0.30,
              columnspacing=0.7, handletextpad=0.4)

    add_panel_label(ax, "b")
    save_panel(fig, "panel_b")


if __name__ == "__main__":
    render()
