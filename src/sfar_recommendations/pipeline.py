"""
Full SFAR pipeline: scrape -> convert -> feed.

1. sfar-scrape: fetch the live index, download new documents to <output>/pdfs/.
2. sfar-convert: OCR PDFs that have no <output>/chandra/ folder yet.
3. sfar-feed: rebuild <output>/feed.xml from <output>/discovery.json.

Every step skips work already on disk, so a re-run only processes what is new.
A scrape that completes but is not comprehensive (known dead upstream links)
does not stop the pipeline; a hard scrape failure does.

Usage (from the repository root):
    uv run sfar-pipeline
    uv run sfar-pipeline --skip-convert     # no OCR (e.g. no GPU available)
    uv run sfar-pipeline --help
"""

import argparse
import sys
from pathlib import Path

from . import convert, feed, scrape


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="sfar-pipeline",
        description="Run sfar-scrape, sfar-convert and sfar-feed in sequence.",
    )
    scrape.add_common_args(parser)
    convert.add_common_args(parser)
    parser.add_argument("--skip-convert", action="store_true",
                        help="Do not run the chandra OCR step.")
    args = parser.parse_args(argv)

    print("=== 1/3 scrape ===")
    scrape_rc = scrape.run_from_args(args)
    if scrape_rc == scrape.EXIT_FAILED:
        print("❌ Scrape failed; stopping.")
        return scrape_rc
    if scrape_rc == scrape.EXIT_INCOMPLETE:
        print("⚠️  Scrape not comprehensive (see completeness_report.txt); continuing.")

    convert_rc = 0
    if args.skip_convert:
        print("\n=== 2/3 convert (skipped) ===")
    else:
        print("\n=== 2/3 convert ===")
        convert_rc = convert.run_from_args(
            argparse.Namespace(output=args.output, chandra_cmd=args.chandra_cmd,
                               dry_run=False))

    print("\n=== 3/3 feed ===")
    feed_rc = feed.main(["--input", str(Path(args.output) / "discovery.json")])

    return max(scrape_rc, convert_rc, feed_rc)


if __name__ == "__main__":
    sys.exit(main())
