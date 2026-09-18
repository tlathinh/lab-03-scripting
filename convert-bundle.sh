#!/bin/bash
set -euo pipefail

curl -o lab3-bundle.tar.gz "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"

tar -xzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > converted.csv

DATA_ROWS=$(($(wc -l < cleaned.tsv) - 1))
echo "Number of data rows: $DATA_ROWS"

tar -czf converted-archive.tar.gz converted.csv
