"""
make_fig7a.py — Panel (a): kymograph J(x, tau) of the spinodal
decomposition.

Cache: data/fig7/panel_a.npz
Render: Figure/fig7/panel_a.{pdf,png}
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
CACHE = os.path.join(DATA_DIR, "panel_a.npz")


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    d = load_or_compute()
    np.savez(CACHE, x=d["x"], t=d["t"], J=d["J"])
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax, cax = new_panel_fig(with_cbar=True)

    x = d["x"]; t = d["t"]; J = d["J"]
    vmin = float(np.percentile(J, 2))
    vmax = float(np.percentile(J, 98))
    im = ax.imshow(J, origin="lower", aspect="auto",
                   extent=[t[0], t[-1], x[0], x[-1]],
                   cmap="RdBu_r", vmin=vmin, vmax=vmax,
                   rasterized=True)
    cb = fig.colorbar(im, cax=cax)
    cb.ax.tick_params(labelsize=6)
    cb.ax.set_title(r"$J$", fontsize=7, pad=2)

    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$x/H_0$")
    ax.tick_params(direction="out", length=2.2)

    add_panel_label(ax, "a")
    save_panel(fig, "panel_a")


if __name__ == "__main__":
    render()
