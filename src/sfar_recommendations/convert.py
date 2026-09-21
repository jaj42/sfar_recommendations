"""
OCR conversion of the downloaded SFAR PDFs with chandra.

Every PDF under <output>/pdfs/<year>/ whose output folder
<output>/chandra/<year>/<stem>/ does not exist yet is converted, so re-runs only
convert new documents. Non-PDF documents (.docx, .xlsx, ...) are not converted.

chandra accepts a directory and loads the model once for all files in it, so
the pending PDFs of each year are symlinked into a temporary directory and
converted with a single ``chandra.sh <tmpdir> <output>/chandra/<year>`` call
(one model load per year rather than per PDF).

Usage (from the repository root):
    uv run sfar-convert              # convert every PDF that has no chandra output yet
    uv run sfar-convert --dry-run    # list what would be converted
    uv run sfar-convert --help
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

DEFAULT_OUTPUT_DIR = Path("output")
DEFAULT_CHANDRA_CMD = "chandra.sh"


def pending_conversions(output_dir):
    """Yield (pdf, year_out_dir) for every PDF with no chandra output folder."""
    pdfs_dir = output_dir / "pdfs"
    chandra_dir = output_dir / "chandra"
    for year_dir in sorted(p for p in pdfs_dir.iterdir() if p.is_dir()):
        year_out = chandra_dir / year_dir.name
        for pdf in sorted(year_dir.rglob("*")):
            if pdf.is_file() and pdf.suffix.lower() == ".pdf":
                if not (year_out / pdf.stem).is_dir():
                    yield pdf, year_out


def run_from_args(args):
    """Convert pending PDFs; return an exit code (1 if any conversion failed)."""
    output_dir = Path(args.output)
    if not (output_dir / "pdfs").is_dir():
        print(f"ERROR: {output_dir / 'pdfs'} not found; run sfar-scrape first.")
        return 1

    pending = list(pending_conversions(output_dir))
    print(f"🔎 {len(pending)} PDF(s) without chandra output.")
    if args.dry_run:
        for pdf, year_out in pending:
            print(f"  would convert: {pdf} -> {year_out}")
        return 0
    if pending and shutil.which(args.chandra_cmd) is None:
        print(f"ERROR: '{args.chandra_cmd}' not found on PATH (see --chandra-cmd).")
        return 1

    by_year = defaultdict(list)
    for pdf, year_out in pending:
        by_year[year_out].append(pdf)

    failed = []
    for i, (year_out, pdfs) in enumerate(sorted(by_year.items()), start=1):
        print(f"[{i}/{len(by_year)}] convert {len(pdfs)} PDF(s) -> {year_out}", flush=True)
        year_out.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="sfar-convert-") as tmp:
            for pdf in pdfs:
                (Path(tmp) / pdf.name).symlink_to(pdf.resolve())
            result = subprocess.run([args.chandra_cmd, tmp, str(year_out)])
        # chandra keeps going after a per-file error, so check each output folder.
        for pdf in pdfs:
            if not (year_out / pdf.stem).is_dir():
                print(f"  ❌ conversion failed (exit {result.returncode}): {pdf}")
                failed.append(pdf)

    print(f"✅ Converted {len(pending) - len(failed)}/{len(pending)} PDF(s).")
    for pdf in failed:
        print(f"  failed: {pdf}")
    return 1 if failed else 0


def add_common_args(parser):
    """Converter options, shared with sfar-pipeline (which has its own --output)."""
    parser.add_argument("--chandra-cmd", type=str, default=DEFAULT_CHANDRA_CMD,
                        help=f"OCR command, called as CMD <input-dir> <outdir> "
                             f"(default: {DEFAULT_CHANDRA_CMD}).")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="sfar-convert",
        description="OCR the downloaded PDFs with chandra, skipping those already converted.",
    )
    parser.add_argument("--output", type=str, default=str(DEFAULT_OUTPUT_DIR),
                        help=f"Output directory holding pdfs/ and chandra/ "
                             f"(default: {DEFAULT_OUTPUT_DIR}).")
    parser.add_argument("--dry-run", action="store_true",
                        help="List the PDFs that would be converted, then exit.")
    add_common_args(parser)
    return run_from_args(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
