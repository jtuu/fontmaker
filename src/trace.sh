#!/bin/bash
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"
convert "$1" -scale 400% bmp:- | potrace --svg -a 0 -n > "$2/$filename.svg"
