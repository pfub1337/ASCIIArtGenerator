# ASCIIArtGenerator
This program was created for converting .jpg image into ASCII art.

_config.txt_ had some easy settings:

```
chars - symbols used to draw in order from brightest to darkest. String;
scaleMultiply - image resolution multiplier. Float;
charWidth and chaarHeight - the width and height of the symbol. This setting is for changing the image resolution correctly. Integers;
fontPath - path to the font file. String;
fontSize - font size. Integer;
imgName - name of the source image. String.
```
To convert an image to ASCII, you need to move the original image to the program folder, rename the image to _source.jpg_ or the name that is specified in the _config.txt_, then run the program.
