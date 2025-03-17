#!/bin/bash

# Check if arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 input_directory output_file.txt"
  exit 1
fi

# Get input directory and output file
input_dir="$1"
output_file="$2"

# Check if input directory exists
if [ ! -d "$input_dir" ]; then
  echo "Error: Directory '$input_dir' not found."
  exit 1
fi

# Create or clear the output file
> "$output_file"

# Get all files in the directory
files=($(find "$input_dir" -type f | sort))

# Check if any files were found
if [ ${#files[@]} -eq 0 ]; then
  echo "No files found in directory '$input_dir'."
  exit 1
fi

# Process each file
total_files=${#files[@]}
counter=0

for file in "${files[@]}"; do
  counter=$((counter+1))
  
  # Append file content to output file
  cat "$file" >> "$output_file"
  
  # Add separator after each file (except the last one)
  if [ $counter -lt $total_files ]; then
    echo "------" >> "$output_file"
  fi
done

echo "All $total_files files from '$input_dir' have been combined into '$output_file'"