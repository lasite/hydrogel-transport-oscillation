"""
fig7_style.py — Canonical per-panel size + axes rectangle for Fig 7
(spinodal verification, appendix).

Same canonical 2.7 × 2.7 in panel as fig 1–6.
"""
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import matplotlib.pyplot as plt
from style_pub import set_style as _set_style_base


PANEL_W = 2.7
PANEL_H = 2.7
DPI_PNG = 300
DPI_PDF = 600

AXES_LEFT   = 0.2607
AXES_BOTTOM = 0.1970
AXES_WIDTH  = 0.5511
AXES_HEIGHT = 0.6578
AXES_RECT   = (AXES_LEFT, AXES_BOTTOM, AXES_WIDTH, AXES_HEIGHT)

CBAR_LEFT  = 0.83
CBAR_WIDTH = 0.03
CBAR_RECT  = (CBAR_LEFT, AXES_BOTTOM, CBAR_WIDTH, AXES_HEIGHT)

LABEL_X = 0.04
LABEL_Y = 0.95
LABEL_FONTSIZE = 10

FIG_DIR = os.path.normpath(os.path.join(_HERE, "..", "Figure", "fig7"))


def set_style():
    _set_style_base()
    plt.rcParams.update({
        "axes.labelsize": 8,
        "xtick.labelsize": 6.5,
        "ytick.labelsize": 6.5,
        "legend.fontsize": 5.5,
        "savefig.bbox": "standard",
        "savefig.pad_inches": 0,
    })


def new_panel_fig(with_cbar=False):
    fig = plt.figure(figsize=(PANEL_W, PANEL_H))
    ax = fig.add_axes(AXES_RECT)
    if with_cbar:
        cax = fig.add_axes(CBAR_RECT)
        return fig, ax, cax
    return fig, ax


def add_panel_label(ax, label):
    fig = ax.figure
    fig.text(LABEL_X, LABEL_Y, f"({label})",
             fontsize=LABEL_FONTSIZE, fontweight='bold',
             va='top', ha='left')


def save_panel(fig, name):
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, name)
    fig.savefig(out + ".pdf", dpi=DPI_PDF, bbox_inches=None, pad_inches=0)
    fig.savefig(out + ".png", dpi=DPI_PNG, bbox_inches=None, pad_inches=0)
    plt.close(fig)
    print(f"  Saved: {out}.pdf / .png")
