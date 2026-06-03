"""
make_fig7.py — Composite tiler for Fig 7 (2×2 mosaic).

Spinodal-decomposition appendix figure. Same pypdf+imshow pattern as
make_fig2/4/6.
"""
import os
import sys
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.image import imread

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from fig7_style import FIG_DIR, PANEL_W, PANEL_H, DPI_PNG

LAYOUT = [['panel_a', 'panel_b'],
          ['panel_c', 'panel_d']]


def _check(ext):
    for row in LAYOUT:
        for name in row:
            path = os.path.join(FIG_DIR, f"{name}.{ext}")
            if not os.path.exists(path):
                raise FileNotFoundError(
                    f"missing {path} — run make_fig7{name[-1]}.py first")


def _build_png():
    _check("png")
    nrows, ncols = len(LAYOUT), len(LAYOUT[0])
    fig = plt.figure(figsize=(PANEL_W * ncols, PANEL_H * nrows))
    for r in range(nrows):
        for c in range(ncols):
            png = os.path.join(FIG_DIR, f"{LAYOUT[r][c]}.png")
            ax = fig.add_subplot(nrows, ncols, r * ncols + c + 1)
            ax.imshow(imread(png))
            ax.set_axis_off()
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0,
                        wspace=0.0, hspace=0.0)
    out_png = os.path.join(FIG_DIR, "fig7.png")
    fig.savefig(out_png, dpi=DPI_PNG, bbox_inches=None, pad_inches=0)
    plt.close(fig)
    print(f"  Saved raster composite: {out_png}")


def _build_pdf():
    from pypdf import PdfWriter, PdfReader
    _check("pdf")
    nrows, ncols = len(LAYOUT), len(LAYOUT[0])
    pt_per_in = 72.0
    page_w = PANEL_W * ncols * pt_per_in
    page_h = PANEL_H * nrows * pt_per_in
    writer = PdfWriter()
    blank = writer.add_blank_page(width=page_w, height=page_h)
    for r in range(nrows):
        for c in range(ncols):
            pdf_in = os.path.join(FIG_DIR, f"{LAYOUT[r][c]}.pdf")
            page_in = PdfReader(pdf_in).pages[0]
            tx = c * PANEL_W * pt_per_in
            ty = (nrows - 1 - r) * PANEL_H * pt_per_in
            blank.merge_translated_page(page_in, tx, ty)
    out_pdf = os.path.join(FIG_DIR, "fig7.pdf")
    with open(out_pdf, "wb") as fh:
        writer.write(fh)
    print(f"  Saved vector composite: {out_pdf}")


def _publish():
    pub_dir = os.path.normpath(os.path.join(_HERE, "..", "Figure", "pub"))
    os.makedirs(pub_dir, exist_ok=True)
    for ext in ("pdf", "png"):
        src = os.path.join(FIG_DIR, f"fig7.{ext}")
        dst = os.path.join(pub_dir, f"fig7.{ext}")
        shutil.copyfile(src, dst)
    print(f"  Published to: {pub_dir}/fig7.{{pdf,png}}")


def main():
    _build_pdf()
    _build_png()
    _publish()


if __name__ == "__main__":
    main()
