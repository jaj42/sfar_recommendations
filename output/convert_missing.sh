#!/bin/sh
# Convert every PDF under pdfs/<year>/ with chandra.sh, skipping any whose
# output folder already exists under chandra/<year>/.

set -u

for year in pdfs/*/; do
    year=$(basename "$year")
    find "pdfs/${year}" -iname '*.pdf' | while IFS= read -r pdf; do
        base=$(basename "$pdf")
        base=${base%.[Pp][Dd][Ff]}
        out="chandra/${year}/${base}"
        if [ -d "$out" ]; then
            echo "skip (exists): $out"
        else
            echo "convert: $pdf -> chandra/${year}"
            chandra.sh "$pdf" "chandra/${year}"
        fi
    done
done
