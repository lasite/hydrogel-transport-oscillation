"""Run bounded root-cause diagnostics for missing canonical oscillations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .root_cause import run_root_cause_suite


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        default="results/root_cause_missing_oscillations",
        help="Directory for diagnostic-only root-cause outputs.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing diagnostic output directory.",
    )
    args = parser.parse_args()
    outdir = Path(args.outdir)
    summary = run_root_cause_suite(outdir, overwrite=args.overwrite)
    print(
        json.dumps(
            {
                "summary": str(outdir / "suite_summary.json"),
                "conclusion_label": summary["conclusion_label"],
                "case_count": len(summary["rows"]),
                "paper_evidence_status": summary["paper_evidence_status"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
