"""
make_fig2c.py — Panel (c): surface oscillation period in the LCST-front
regime, on (Bi_T, S_chi).

Cache: data/fig2/panel_c.npz
Render: Figure/fig2/panel_c.{pdf,png}

Log colour scale exposes the SNIC period divergence at the upper- and
lower-S_chi boundaries of the LCST-front region. Non-oscillating cells
(steady cold / frozen front / failed) are masked to a neutral grey.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig2_style import (
    set_style, new_panel_fig, save_panel, add_panel_label, wp_marker,
)
from fig2_data import WORKING_POINT
from fig4_data import (build_grid, BI_T_VALS, S_CHI_VALS,
                       REG_LCST_FRONT, REG_BULK_HOPF, REG_GLOBAL_COLLAPSE)

DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data", "fig2"))
CACHE = os.path.join(DATA_DIR, "panel_c.npz")


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    g = build_grid(param_x="Bi_T", x_vals=BI_T_VALS,
                   param_y="S_chi", y_vals=S_CHI_VALS, verbose=False)
    osc = ((g["regime"] == REG_LCST_FRONT) |
           (g["regime"] == REG_BULK_HOPF) |
           (g["regime"] == REG_GLOBAL_COLLAPSE))
    P = np.where(osc & np.isfinite(g["period"]) & (g["period"] > 0),
                 g["period"], np.nan)
    np.savez(CACHE,
             Bi_T=g["x"], S_chi=g["y"], period=P,
             wp_Bi_T=np.float64(WORKING_POINT["Bi_T"]),
             wp_S_chi=np.float64(WORKING_POINT["S_chi"]))
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    P = d["period"]
    set_style()
    fig, ax, cax = new_panel_fig(with_cbar=True)

    finite = np.isfinite(P)
    if not finite.any():
        ax.text(0.5, 0.5, "no oscillating cells", ha="center", va="center",
                transform=ax.transAxes, fontsize=8)
        save_panel(fig, "panel_c")
        return
    vmin = float(np.nanmin(P[finite]))
    vmax = float(np.nanmax(P[finite]))
    cmap = plt.get_cmap("plasma_r").copy()
    cmap.set_bad("#ececec")  # non-oscillating cells -> neutral grey

    from matplotlib.ticker import FuncFormatter, FixedLocator, NullLocator
    pcm = ax.pcolormesh(d["Bi_T"], d["S_chi"], P,
                        cmap=cmap, norm=LogNorm(vmin=vmin, vmax=vmax),
                        shading="nearest", rasterized=True)
    cb = fig.colorbar(pcm, cax=cax)
    # Periods are O(1)–O(50); plain integer ticks read cleanly inside the
    # narrow right margin (sci-notation `4 × 10^1` overflows). Pin the
    # tick positions inside [vmin, vmax] so we never see sci-notation.
    candidates = [5, 8, 10, 15, 20, 30, 40, 50, 75, 100]
    ticks = [t for t in candidates if vmin <= t <= vmax]
    cb.ax.yaxis.set_major_locator(FixedLocator(ticks))
    cb.ax.yaxis.set_minor_locator(NullLocator())
    cb.ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}"))
    cb.ax.tick_params(labelsize=6)
    cb.ax.set_title(r"$T_\mathrm{PDE}$", fontsize=7, pad=2)

    wp_marker(ax, float(d["wp_Bi_T"]), float(d["wp_S_chi"]))
    ax.set_xscale("log")
    ax.set_xlabel(r"$\mathrm{Bi}_T$")
    ax.set_ylabel(r"$S_\chi$")
    ax.set_xlim(d["Bi_T"].min(), d["Bi_T"].max())
    ax.set_ylim(d["S_chi"].min(), d["S_chi"].max())
    ax.tick_params(direction="out", length=2.2)

    add_panel_label(ax, "c")
    save_panel(fig, "panel_c")


if __name__ == "__main__":
    render()
