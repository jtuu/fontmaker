#!/bin/python
import os
import sys
import fontforge

def make_font(out_filename, in_filenames):
    (fontname, out_type) = os.path.splitext(os.path.basename(out_filename))
    out_type = out_type[1:]
    font = fontforge.font()
    font.fullname = font.familyname = font.fontname = fontname
    font.em = 1024
    for filename in in_filenames:
        charcode = ord(os.path.splitext(os.path.basename(filename))[0])
        char = font.createChar(charcode)
        char.importOutlines(filename)
    font.generate(out_filename, bitmap_type = out_type)

if __name__ == "__main__":
    out_filename = sys.argv[1]
    in_filenames = sys.argv[2:]
    if len(in_filenames) > 0:
        make_font(out_filename, in_filenames)
