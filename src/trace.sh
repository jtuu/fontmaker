#!/bin/bash
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"
escaped=$(sed -r "s/(\?|\*)/\\\\\1/g" <<< "$1")
convert "$escaped" -scale 400% bmp:- | potrace --svg -a 0 -n > "$2/$filename.svg"
