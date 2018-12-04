# fontmaker
Raster image to TrueType font converter

## Dependencies
* GIMP 2.10
* FontForge 2017
* potrace 1.15
* ImageMagick 7
* Bash 4
* Python 3

## Usage
`./src/fontmaker.sh /path/to/inputfile`

**Inputfile** must be a graphics container file (probably .xcf) containing the characters to be used to make the font. Each character must be on a separate layer and the layer must be named the character that it represents. Fontmaker creates a new directory where the input file is located. The resulting font file will be output there along with 2 subdirectories ("raster" containing the characters as individual files and "vector" containing the vectorized characters).
