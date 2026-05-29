from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DERIVATIONS_DIR = ROOT / "docs" / "derivations"
RENDERED_DIR = ROOT / "docs" / "rendered"


def main() -> int:
    tex_files = sorted(DERIVATIONS_DIR.glob("*.tex"))
    if not tex_files:
        print("Warning: no derivation .tex files found.")
        return 0

    if shutil.which("latexmk") is None:
        print(
            "Warning: latexmk not found; skipping derivation build in exploratory scaffold stage."
        )
        return 0

    RENDERED_DIR.mkdir(parents=True, exist_ok=True)

    for tex_file in tex_files:
        cmd = [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-outdir={RENDERED_DIR}",
            str(tex_file),
        ]
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode != 0:
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
