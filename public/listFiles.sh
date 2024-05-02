#!/bin/bash

# RUN ME LIKE THIS: `./listFiles.sh ./public/pages`

# Check if a destination folder is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <destination_folder>"
    exit 1
fi

# Destination folder provided as argument
destination_folder="$1"

# Navigate to the destination folder
cd "$destination_folder" || { echo "Error: Destination folder not found"; exit 1; }

# Get the current folder name
current_folder=$(basename "$(pwd)")

# Loop through each file in the directory
for file in *; do
    # Check if the file is a regular file (not a directory)
    if [ -f "$file" ]; then
        # Get the file name without extension
        filename=$(basename -- "$file")
        # Get the file extension
        extension="${filename##*.}"
        # Form the output string with both current and destination folder
        output="'$destination_folder/$filename',"
        # Print the formatted output
        echo "$output"
    fi
done

