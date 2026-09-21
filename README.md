# SFAR Recommendations Scraper

Targeted crawler that discovers every SFAR (Société Française d'Anesthésie-Réanimation)
clinical recommendation, downloads the document(s), OCRs the PDFs to Markdown/HTML with
chandra, and writes an XLSX manifest for human curation plus an Atom feed. Most documents are
PDFs; the occasional Office document (`.docx`, `.xlsx`, …) is downloaded too. Loose image scans
are **not** downloaded (they are reported as misses).

## Project layout

| Path | Contents |
| --- | --- |
| `src/sfar_recommendations/` | The Python package: `scrape.py`, `convert.py`, `feed.py`, `pipeline.py` |
| `reference/` | Offline snapshot of the index (`Recommandations - La SFAR.html`) and the reference title list (`Recommandations - La SFAR.md`) used by the completeness check |
| `output/` | Everything the pipeline produces (see [Outputs](#outputs)); PDFs are tracked with Git LFS |

## Install / run (uv)

```bash
uv sync                          # create the venv from pyproject.toml + uv.lock
```

All commands are meant to be run from the repository root (default paths are relative to it).

```bash
uv run sfar-pipeline                # scrape + convert + feed, only processing what is new

uv run sfar-scrape                  # discover + resolve + download + verify
uv run sfar-scrape --dry-run        # discover + resolve + manifest, no downloads
uv run sfar-scrape --verify-only    # re-run the completeness check on existing discovery.json
uv run sfar-convert                 # OCR every PDF that has no chandra output yet
uv run sfar-convert --dry-run       # list the PDFs that would be converted
uv run sfar-feed                    # build feed.xml (Atom) from an existing discovery.json
```

Every command accepts `--help`. Useful options:

- `sfar-scrape` / `sfar-pipeline`: `--index-html PATH` (read an offline snapshot instead of the
  live index), `--reference-md PATH`, `--workers N` (default 6), `--delay SECONDS` (default 0.5),
  `--output DIR` (default `output`).
- `sfar-convert` / `sfar-pipeline`: `--chandra-cmd CMD` (default `chandra.sh`, called as
  `CMD <input-dir> <outdir>`, once per year so the model is loaded once per batch).
  `sfar-pipeline --skip-convert` skips the OCR step.
- `sfar-feed`: `--input`, `--output`, `--all`.

Note that `sfar-scrape --dry-run` rewrites `discovery.json` without filenames, so the next real
run can no longer skip files without a request. Point it at a scratch directory
(`--output /tmp/sfar-dry`) to preview what is new.

## Pipeline

`sfar-pipeline` runs three steps. Each one skips work that is already on disk, so a re-run only
processes new recommendations.

1. **Scrape** (`sfar-scrape`): fetch the live index, resolve every row to its documents, and
   download new ones to `output/pdfs/<year>/`.
2. **Convert** (`sfar-convert`): for each `output/pdfs/<year>/<name>.pdf` without an
   `output/chandra/<year>/<name>/` folder, run chandra to produce Markdown, HTML and extracted
   images there. The pending PDFs of a year are converted in one chandra call (symlinked into a
   temporary directory), so the model is loaded once per year rather than once per PDF.
   Non-PDF documents are not converted.
3. **Feed** (`sfar-feed`): rebuild `output/feed.xml` from `output/discovery.json`.

A scrape that completes but is not comprehensive (the known dead upstream links, see below) does
not stop the pipeline; a hard failure (index unreachable, nothing discovered) does. The pipeline
exits non-zero if any step reported a problem.

## How the scraper works

Discovery fetches the **live** recommendations index (`https://sfar.org/recommandations/`) and
saves a copy to `output/index.html`, so every run records what it saw. If the live fetch fails,
the scraper stops with an error rather than silently using stale data; pass
`--index-html "reference/Recommandations - La SFAR.html"` to work from the offline snapshot
instead. Documents are always fetched from the live site (which serves them fine with browser
headers).

The index lists each recommendation across four tabs (Chronologie, Anesthésie, Réanimation,
Urgences). Each row links to the document in one of three forms, all handled:

1. **Direct PDF**: `/wp-content/uploads/YYYY/MM/<file>.pdf` (SFAR- or HAS-hosted).
2. **WP Download Manager**: the landing page carries an
   `<a class="wpdm-download-link" data-downloadurl=".../download/<slug>/?wpdmdl=<id>">`
   button. The real PDF URL lives in `data-downloadurl`, **not** in the visible `href`
   (which is just `#` or the package landing).
3. **Landing page**: `/slug/` fetched live; all of its download buttons and any non-boilerplate
   direct documents are collected (a single reco can expose several files, e.g. main text +
   argumentaire + appendices). If the landing URL itself redirects straight to a document, that
   file is taken directly.

Footer boilerplate (CGV, règlement intérieur, certificats, chartes…) is filtered out.
Documents are deduplicated by WP Download Manager id (or absolute file URL) and merged across the
tabs they appear in.

Re-runs are **idempotent**: a file already recorded in `discovery.json` and present on disk is
skipped with no network request, so a second run downloads only what is new or was missing.

## Types

Best-effort from the row's CSS class: **RFE**, **RPP**, **Préconisation**. A document is
tagged **HAS** (Haute Autorité de Santé) when it is hosted on `has-sante.fr` or its title
carries an explicit `HAS` token.

## Outputs

All under `output/` by default:

- `pdfs/<year>/<filename>`: downloaded documents (mostly `.pdf`, plus the odd `.docx`/`.xlsx`);
  filename taken from the `Content-Disposition` header (falls back to the URL basename, with the
  extension inferred from the content-type); year `unknown` for docs found only in discipline tabs.
- `chandra/<year>/<name>/`: chandra OCR output for each PDF (`<name>.md`, `<name>.html`,
  `<name>_metadata.json` and the extracted images).
- `index.html`: the live index as fetched by the last scrape.
- `manifest.xlsx`: formatted, filterable manifest (see columns below); `include` is left blank
  for curation.
- `discovery.json`: raw resolved documents plus the list of unresolved rows, for debugging.
- `completeness_report.txt`: see below.
- `feed.xml`: an Atom 1.0 feed of the recommendations that are on disk (downloaded in the latest
  run or an earlier one). Each entry has the title, a link (SFAR landing page, or the direct
  document URL when there is no landing page), the year as its date, and `type`/`discipline`/`year`
  categories. `sfar-feed --all` also includes docs that failed to download.

### Manifest columns
`type` · `discipline` · `subdomain` · `year` · `title` · `landing_url` · `download_url` ·
`wpdmdl` · `filename` · `bytes` · `sha256` · `is_new` · `include`

## Comprehensiveness check

After downloading, the scraper cross-checks that nothing was silently dropped and writes
`completeness_report.txt`:

- **MISS**: index rows that resolved to zero documents (e.g. a HAS *portal* page with no direct
  file, a dead `404` link, or an image-only scan). These are surfaced, not hidden.
- **ERROR**: targets that failed to download: a genuine network/HTTP failure, an empty body, a
  non-document content-type, or a WP Download Manager `Fichier non trouvé` HTML page (an old
  version removed upstream; the current version is downloaded via a sibling link).
- **File types**: a count of what was downloaded, by extension.
- **Coverage**: per-year counts, a check that every year from 2000 to the current year is
  represented (and the current year is non-empty), a diff of discovered titles against
  `reference/Recommandations - La SFAR.md`, and a superset check against a curated `pdfs/` set
  if one exists in the working directory.
- **External**: documents hosted off `sfar.org` (e.g. HAS, Urofrance) listed for a manual check.

`sfar-scrape` exits with 2 if there are unresolved rows or download errors, so an incomplete run
fails visibly (1 means a hard failure). A few residual MISS/ERROR entries are **dead upstream
links** (retired HAS portal pages, `404`s, and superseded WPDM versions) that cannot be fetched
from SFAR at all.
