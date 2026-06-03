"""
fig2_style.py — Canonical per-panel size + axes rectangle for Fig 2
(the nonlinear regime-classification figure).

Mirrors `fig1_style.py` and `fig3_style.py` so panels of the three
figures share font sizes and line weights when downscaled to the APS
``\\textwidth`` block. Fig 2 is a 2×2 mosaic; with the canonical
``2.7 × 2.7`` panel we get a ``5.4 × 5.4 in`` intrinsic composite.

Like fig 3 every panel reserves a fixed colorbar strip in the right
margin (`CBAR_RECT`); profile-only panels simply leave the strip
empty so the tile pixel layout is identical.
"""
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import matplotlib.pyplot as plt
from style_pub import set_style as _set_style_base


# ── Per-panel canonical size (matches fig 1 / fig 3 for cross-figure consistency) ──
PANEL_W = 2.7
PANEL_H = 2.7
DPI_PNG = 300
DPI_PDF = 600

# ── Inner axes rectangle, figure-relative coords (matches fig 1 / fig 3) ──
AXES_LEFT   = 0.2607
AXES_BOTTOM = 0.1970
AXES_WIDTH  = 0.5511
AXES_HEIGHT = 0.6578
AXES_RECT   = (AXES_LEFT, AXES_BOTTOM, AXES_WIDTH, AXES_HEIGHT)

# ── Colorbar rectangle (used by panels with a categorical or scalar cbar) ──
CBAR_LEFT  = 0.83
CBAR_WIDTH = 0.03
CBAR_RECT  = (CBAR_LEFT, AXES_BOTTOM, CBAR_WIDTH, AXES_HEIGHT)

# ── Panel label (figure-relative coords) ──
LABEL_X = 0.04
LABEL_Y = 0.95
LABEL_FONTSIZE = 10

# ── Output directory ──
FIG_DIR = os.path.normpath(os.path.join(_HERE, "..", "Figure", "fig2"))


# ── Regime palette (shared across fig 2 panels (a) and (b)) ──
# Codes match fig4_data.REG_*: -1 failed, 0 cold, 2 LCST front, 5 frozen front.
# Other codes (1 bulk_hopf, 3 global_collapse, 4 steady_collapsed) are not
# realised in either default-IC sweep, so they are listed in the legend only
# for completeness.
REG_COLORS = {
    -1: "#cccccc",   # failed (solver / SNIC integration window exceeded)
     0: "#cfe7ff",   # steady cold (Flory–Huggins swollen branch)
     1: "#7fbf7b",   # bulk Hopf (not realised; reserved colour)
     2: "#d6604d",   # LCST front (the relaxation oscillator)
     3: "#762a83",   # global collapse oscillation (not realised; reserved)
     4: "#3a1f73",   # uniform collapsed (not realised; reserved)
     5: "#fed98e",   # frozen partial-collapse front
}
REG_LABELS = {
    -1: "failed (SNIC)",
     0: "steady cold",
     1: "bulk Hopf",
     2: "LCST front",
     3: "global collapse",
     4: "uniform collapsed",
     5: "frozen front",
}


def set_style():
    """Project base style + panel-uniformity overrides."""
    _set_style_base()
    plt.rcParams.update({
        "axes.labelsize": 8,
        "xtick.labelsize": 6.5,
        "ytick.labelsize": 6.5,
        "legend.fontsize": 5.5,
        # CRITICAL: style_pub sets savefig.bbox='tight' which auto-trims
        # whitespace per panel, producing PNGs of inconsistent pixel sizes.
        # Standard bbox keeps every panel at exactly figsize × DPI px.
        "savefig.bbox": "standard",
        "savefig.pad_inches": 0,
    })


def new_panel_fig(with_cbar=False):
    """Return ``(fig, ax)`` or ``(fig, ax, cax)`` with absolutely-positioned
    axes (and optional colorbar). Same axes pixel rectangle in every panel."""
    fig = plt.figure(figsize=(PANEL_W, PANEL_H))
    ax = fig.add_axes(AXES_RECT)
    if with_cbar:
        cax = fig.add_axes(CBAR_RECT)
        return fig, ax, cax
    return fig, ax


def add_panel_label(ax, label):
    """Place ``(x)`` panel label at fixed figure-relative coords."""
    fig = ax.figure
    fig.text(LABEL_X, LABEL_Y, f"({label})",
             fontsize=LABEL_FONTSIZE, fontweight='bold',
             va='top', ha='left')


def save_panel(fig, name):
    """Save panel without ``bbox_inches='tight'`` so all PNGs have identical
    ``(PANEL_W*DPI_PNG, PANEL_H*DPI_PNG)`` pixel dimensions."""
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, name)
    fig.savefig(out + ".pdf", dpi=DPI_PDF, bbox_inches=None, pad_inches=0)
    fig.savefig(out + ".png", dpi=DPI_PNG, bbox_inches=None, pad_inches=0)
    plt.close(fig)
    print(f"  Saved: {out}.pdf / .png")


def wp_marker(ax, xv, yv, label="WP"):
    """Working-point star + small annotation, used by every (Bi_T,*) panel."""
    ax.scatter([xv], [yv], s=42, marker="*", color="white",
               edgecolor="k", linewidth=0.7, zorder=8)
    if label:
        ax.annotate(label, (xv, yv), xytext=(4, 3),
                    textcoords="offset points", fontsize=5.5,
                    color="0.10", zorder=9)
