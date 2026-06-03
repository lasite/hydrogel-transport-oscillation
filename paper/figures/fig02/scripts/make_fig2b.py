"""
make_fig2b.py — Panel (b): regime classification on (Bi_T, Da) at S_chi=WP.

Cache: data/fig2/panel_b.npz  (subset of data/fig4/fig4_grid_Bi_T_Da.npz)
Render: Figure/fig2/panel_b.{pdf,png}

This panel confirms that the LCST-front regime persists over more than
a decade in reactivity Da; the Bi_T axis is shared with panel (a) and
the working-point S_chi=1.0 is fixed.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.lines import Line2D

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig2_style import (
    set_style, new_panel_fig, save_panel, add_panel_label,
    REG_COLORS, REG_LABELS, wp_marker,
)
from fig2_data import WORKING_POINT
from fig4_data import build_grid, BI_T_VALS, DA_VALS

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig2"))
CACHE = os.path.join(DATA_DIR, "panel_b.npz")


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    g = build_grid(param_x="Bi_T", x_vals=BI_T_VALS,
                   param_y="Da", y_vals=DA_VALS, verbose=False)
    np.savez(CACHE,
             Bi_T=g["x"], Da=g["y"], regime=g["regime"],
             wp_Bi_T=np.float64(WORKING_POINT["Bi_T"]),
             wp_Da=np.float64(WORKING_POINT["Da"]),
             wp_S_chi=np.float64(WORKING_POINT["S_chi"]))
    print(f"  Saved cache: {CACHE}")


def _categorical_pcolormesh(ax, x, y, reg):
    codes = sorted(REG_COLORS.keys())
    cmap = ListedColormap([REG_COLORS[c] for c in codes])
    norm = BoundaryNorm([c - 0.5 for c in codes] + [codes[-1] + 0.5], cmap.N)
    return ax.pcolormesh(x, y, reg, cmap=cmap, norm=norm,
                         shading="nearest", rasterized=True)


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax = new_panel_fig()

    _categorical_pcolormesh(ax, d["Bi_T"], d["Da"], d["regime"])
    wp_marker(ax, float(d["wp_Bi_T"]), float(d["wp_Da"]))

    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"$\mathrm{Bi}_T$")
    ax.set_ylabel(r"$\mathrm{Da}$")
    ax.set_xlim(d["Bi_T"].min(), d["Bi_T"].max())
    ax.set_ylim(d["Da"].min(), d["Da"].max())
    ax.tick_params(direction="out", length=2.2)

    ax.text(0.03, 0.97,
            rf"$S_\chi={float(d['wp_S_chi']):.2f}$",
            transform=ax.transAxes, ha="left", va="top",
            fontsize=6.5,
            bbox=dict(facecolor="white", edgecolor="0.5",
                      boxstyle="round,pad=0.18", lw=0.4))

    present = sorted({int(c) for c in d["regime"].flatten()})
    handles = [Line2D([0], [0], marker='s', linestyle='',
                      color=REG_COLORS[c], markeredgecolor="0.4",
                      markeredgewidth=0.4, markersize=6,
                      label=REG_LABELS[c]) for c in present]
    ax.legend(handles=handles, loc="lower right",
              framealpha=0.9, handlelength=1.0, borderpad=0.30,
              labelspacing=0.30, handletextpad=0.4)

    add_panel_label(ax, "b")
    save_panel(fig, "panel_b")


if __name__ == "__main__":
    render()
