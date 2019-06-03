#!/bin/sh
set -e
#INPUT_FILE="/drop.json"
INPUT_FILE="drop_dataset_dev.json"
ARCHIVE_FILE="https://oscar-cse481n-19sp.s3.amazonaws.com/model.tar.gz"
python predict.py --archive_file $ARCHIVE_FILE  --input_file $INPUT_FILE  --output_file /results/predictions.json
