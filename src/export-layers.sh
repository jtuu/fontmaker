#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)"
in_filename=$(readlink -f "$1")
out_dirname=$(readlink -f "$2")
script_src=$(cat "$DIR/export-layers.scm"; echo -e "\n\n(export-layers \"$in_filename\" \"$out_dirname\")")
gimp --no-data --no-fonts -i -b "$script_src" -b "(gimp-quit 0)"
