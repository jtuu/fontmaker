#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)"
fontname=$(basename -- "$1")
fontname="${fontname%.*}"
out_dirname="$(dirname "$1")/$fontname/"
raster_dir="$out_dirname/raster/"
vector_dir="$out_dirname/vector/"
mkdir -p "$raster_dir"
mkdir -p "$vector_dir"
"$DIR/export-layers.sh" "$1" "$raster_dir" &&
find "$raster_dir" -type f -exec "$DIR/trace.sh" "{}" "$vector_dir" \; &&
find "$vector_dir" -type f -exec "$DIR/gen-font.py" "$out_dirname/$fontname.ttf" {} +
