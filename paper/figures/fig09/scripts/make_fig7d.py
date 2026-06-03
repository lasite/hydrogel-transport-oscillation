"""
make_fig7d.py — Panel (d): Fourier power spectrum |J^(k)|^2 at
selected times.

Cache: data/fig7/panel_d.npz
Render: Figure/fig7/panel_d.{pdf,png}
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
CACHE = os.path.join(DATA_DIR, "panel_d.npz")
N_PROFILES = 6


def compute():
    os.makedirs(DATA_DIR, exist_ok=True)
    d = load_or_compute()
    x = d["x"]; t = d["t"]; J = d["J"]
    Nx = len(x)
    k_arr = np.fft.rfftfreq(Nx, d=1.0 / Nx) * 2 * np.pi

    t_idx = np.linspace(0, len(t) - 1, N_PROFILES).astype(int)[1:]
    spectra = []
    for i in t_idx:
        Jc = J[:, i] - J[:, i].mean()
        spectra.append(np.abs(np.fft.rfft(Jc)) ** 2)
    spectra = np.asarray(spectra)
    np.savez(CACHE,
             k=k_arr, t=t[t_idx], spectra=spectra,
             k_star=np.float64(d["k_star"]))
    print(f"  Saved cache: {CACHE}")


def render():
    if not os.path.exists(CACHE):
        compute()
    d = np.load(CACHE)
    set_style()
    fig, ax = new_panel_fig()

    k = d["k"]; t = d["t"]; sp = d["spectra"]
    kstar = float(d["k_star"])

    colors = plt.cm.viridis(np.linspace(0.1, 0.95, len(t)))
    for i, c in enumerate(colors):
        ax.semilogy(k[1:], sp[i, 1:], color=c, lw=0.7,
                    label=rf"$\tau={t[i]:.3f}$")
    ax.axvline(kstar, color="r", ls=":", lw=0.8,
               label=rf"$k^*={kstar:.0f}$")

    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$|\hat J(k)|^2$")
    ax.set_xlim(0, min(3 * kstar, k[-1]))
    ax.tick_params(direction="out", length=2.2)
    ax.legend(loc="upper right", framealpha=0.85, ncol=2,
              handlelength=1.0, borderpad=0.30, labelspacing=0.30,
              columnspacing=0.7, handletextpad=0.4)

    add_panel_label(ax, "d")
    save_panel(fig, "panel_d")


if __name__ == "__main__":
    render()
