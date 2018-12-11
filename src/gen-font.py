#!/bin/python
import os
import sys
import fontforge

def make_font(out_filename, in_filenames):
    width = 1024
    (fontname, out_type) = os.path.splitext(os.path.basename(out_filename))
    out_type = out_type[1:]
    font = fontforge.font()
    font.fullname = font.familyname = font.fontname = fontname
    font.em = width
    for filename in in_filenames:
        basename = os.path.basename(filename)
        # special case "/" because it's not allowed in filenames
        if basename.startswith("slash"):
            charcode = 47
        elif basename[3] == "." and basename[0] == basename[2]:
            charcode = ord(basename[1])
        elif basename[1] == ".":
            charcode = ord(basename[0])
        else:
            sys.stderr.write("Bad filename, skipping: %s\n" % (basename))
            continue
        char = font.createChar(charcode)
        char.width = width
        # don't import whitespace characters because fontforge doesn't understand empty svg files
        if charcode != 32:
            char.importOutlines(filename)
    font.generate(out_filename, bitmap_type = out_type)

if __name__ == "__main__":
    out_filename = sys.argv[1]
    in_filenames = sys.argv[2:]
    if len(in_filenames) > 0:
        make_font(out_filename, in_filenames)
