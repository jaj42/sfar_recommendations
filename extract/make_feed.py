#!/usr/bin/env python3
"""
Atom feed generator for the SFAR recommendations catalog.

Re-uses the `discovery.json` produced by `scrape_sfar.py` and turns it into an
Atom 1.0 feed (`feed.xml`). No scraping and no network access — it only reads the
JSON already on disk.

Each entry carries the recommendation title, a link (the SFAR landing page, or
the direct document URL when a doc has no landing page), the year as its date,
and Type / Discipline / Year categories.

Usage:
    python make_feed.py                                  # output/discovery.json -> output/feed.xml
    python make_feed.py --input output/discovery.json    # explicit input
    python make_feed.py --all                            # include non-downloaded docs too
    python make_feed.py --help
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "output" / "discovery.json"

ATOM_NS = "http://www.w3.org/2005/Atom"

FEED_TITLE = "SFAR — Recommandations"
FEED_ID = "https://sfar.org/recommandations/"
FEED_ALTERNATE = "https://sfar.org/les-referentiels/"

# Category schemes, so a term like "2026" (year) is never confused with a
# discipline or type term by a strict consumer.
SCHEME_TYPE = "https://sfar.org/ns/type"
SCHEME_DISCIPLINE = "https://sfar.org/ns/discipline"
SCHEME_YEAR = "https://sfar.org/ns/year"


def year_to_date(year):
    """Map a recommendation year to an RFC 3339 timestamp (Jan 1st, UTC)."""
    if year is None:
        return None
    return f"{int(year):04d}-01-01T00:00:00Z"


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def add_category(entry, term, scheme):
    """Append an Atom <category>, but only when the term is truthy."""
    if term:
        ET.SubElement(entry, "category", term=str(term), scheme=scheme)


def build_feed(docs):
    feed = ET.Element("feed", xmlns=ATOM_NS)
    ET.SubElement(feed, "title").text = FEED_TITLE
    ET.SubElement(feed, "id").text = FEED_ID
    ET.SubElement(feed, "link", rel="self", href="feed.xml")
    ET.SubElement(feed, "link", rel="alternate", href=FEED_ALTERNATE)

    dates = [year_to_date(d.get("year")) for d in docs]
    dates = [d for d in dates if d]
    ET.SubElement(feed, "updated").text = max(dates) if dates else now_utc()

    author = ET.SubElement(feed, "author")
    ET.SubElement(author, "name").text = "SFAR"

    for d in docs:
        entry = ET.SubElement(feed, "entry")
        ET.SubElement(entry, "title").text = d.get("title", "")
        ET.SubElement(entry, "id").text = d.get("key") or d.get("download_url", "")

        href = d.get("landing_url") or d.get("download_url", "")
        if href:
            ET.SubElement(entry, "link", rel="alternate", href=href)

        date = year_to_date(d.get("year"))
        if date:
            ET.SubElement(entry, "updated").text = date
            ET.SubElement(entry, "published").text = date

        add_category(entry, d.get("type"), SCHEME_TYPE)
        add_category(entry, d.get("discipline"), SCHEME_DISCIPLINE)
        add_category(entry, d.get("year"), SCHEME_YEAR)

        summary = " · ".join(
            str(p) for p in (d.get("type"), d.get("discipline"), d.get("year")) if p
        )
        if summary:
            ET.SubElement(entry, "summary").text = summary

    return feed


def main():
    parser = argparse.ArgumentParser(
        description="Generate an Atom feed from a scrape_sfar.py discovery.json.",
    )
    parser.add_argument("--input", type=str, default=str(DEFAULT_INPUT),
                        help="discovery.json to read (default: output/discovery.json).")
    parser.add_argument("--output", type=str, default=None,
                        help="Feed file to write (default: feed.xml next to the input).")
    parser.add_argument("--all", action="store_true",
                        help="Include every resolved doc, not just downloaded ones.")
    args = parser.parse_args()

    in_path = Path(args.input).resolve()
    if not in_path.exists():
        print(f"ERROR: {in_path} not found; run scrape_sfar.py first.")
        sys.exit(1)

    out_path = Path(args.output).resolve() if args.output else in_path.parent / "feed.xml"

    data = json.loads(in_path.read_text(encoding="utf-8"))
    docs = data.get("documents", [])
    if not args.all:
        docs = [d for d in docs if d.get("downloaded")]

    # Newest year first, then title (mirrors scrape_sfar.py's manifest sort).
    docs.sort(key=lambda d: (-(d.get("year") or 0), d.get("title", "")))

    feed = build_feed(docs)
    ET.indent(feed)
    ET.ElementTree(feed).write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"📡 Wrote {out_path} ({len(docs)} entries)")


if __name__ == "__main__":
    main()
