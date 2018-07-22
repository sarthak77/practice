from PIL import Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')
"""
The arguments to Image.new() are as follows:

The string 'RGBA', which sets the color mode to RGBA. (There are
other modes that this book doesn’t go into.)
The size, as a two-integer tuple of the new image’s width and height.
The background color that the image should start with, as a
four-integer tuple of an RGBA value. You can use the return value of
the ImageColor.getcolor() function for this argument. Alternatively,
Image.new() also supports just passing the string of the standard
color name.
"""