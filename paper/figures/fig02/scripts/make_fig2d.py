"""
make_fig2d.py — Panel (d): peak polymer fraction max_(xi,t) phi on
(Bi_T, S_chi), with a white LCST contour at phi = 0.5.

Cache: data/fig2/panel_d.npz
Render: Figure/fig2/panel_d.{pdf,png}

The phi = 0.5 contour tracks the cold-vs-front boundary of panel (a),
providing an independent geometric check on the regime classifier.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.colors import Normalize

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig2_style import (
    set_style, new_panel_fig, save_panel, add_panel_label, wp_marker,
)
from fig2_data import WORKING_POINT
from fig4_data import build_grid, BI_T_VALS, S_CHI_VALS

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig2"))
CACHE = os.path.join(DATA_DIR, "panel_d.npz")


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    g = build_grid(param_x="Bi_T", x_vals=BI_T_VALS,
                   param_y="S_chi", y_vals=S_CHI_VALS, verbose=False)
    np.savez(CACHE,
             Bi_T=g["x"], S_chi=g["y"], phi_max=g["phi_max"],
             wp_Bi_T=np.float64(WORKING_POINT["Bi_T"]),
             wp_S_chi=np.float64(WORKING_POINT["S_chi"]))
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax, cax = new_panel_fig(with_cbar=True)

    Z = d["phi_max"]
    pcm = ax.pcolormesh(d["Bi_T"], d["S_chi"], Z,
                        cmap="cividis",
                        norm=Normalize(vmin=0.10, vmax=1.0),
                        shading="nearest", rasterized=True)
    from matplotlib.ticker import MaxNLocator
    cb = fig.colorbar(pcm, cax=cax)
    cb.ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
    cb.ax.tick_params(labelsize=6)
    cb.ax.set_title(r"$\max\,\varphi$", fontsize=7, pad=2)

    # LCST 0.5 contour as an independent check on the regime boundary.
    ax.contour(d["Bi_T"], d["S_chi"], Z, levels=[0.5],
               colors="white", linewidths=1.0, zorder=5)

    wp_marker(ax, float(d["wp_Bi_T"]), float(d["wp_S_chi"]))
    ax.set_xscale("log")
    ax.set_xlabel(r"$\mathrm{Bi}_T$")
    ax.set_ylabel(r"$S_\chi$")
    ax.set_xlim(d["Bi_T"].min(), d["Bi_T"].max())
    ax.set_ylim(d["S_chi"].min(), d["S_chi"].max())
    ax.tick_params(direction="out", length=2.2)

    add_panel_label(ax, "d")
    save_panel(fig, "panel_d")


if __name__ == "__main__":
    render()
