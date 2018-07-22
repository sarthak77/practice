from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
   fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')
im.save('drawing.png')


"""
*Drawing Shapes
The following ImageDraw methods draw various kinds of shapes on the
image. The fill and outline parameters for these methods are optional
and will default to white if left unspecified.

*Points
The point(xy, fill) method draws individual pixels. The xy argument
represents a list of the points you want to draw. The list can be a
list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or
a list of x- and y-coordinates without tuples, such as
[x1, y1, x2, y2, ...]. The fill argument is the color of the points
and is either an RGBA tuple or a string of a color name, such as
'red'. The fill argument is optional.

*Lines
The line(xy, fill, width) method draws a line or series of lines. xy
is either a list of tuples, such as [(x, y), (x, y), ...], or a list
of integers, such as [x1, y1, x2, y2, ...]. Each point is one of the
connecting points on the lines you’re drawing. The optional fill
argument is the color of the lines, as an RGBA tuple or color name.
The optional width argument is the width of the lines and defaults to
1 if left unspecified.

*Rectangles
The rectangle(xy, fill, outline) method draws a rectangle. The xy
argument is a box tuple of the form (left, top, right, bottom). The
left and top values specify the x- and y-coordinates of the upper-left
corner of the rectangle, while right and bottom specify the lower-right
corner. The optional fill argument is the color that will fill the
inside of the rectangle. The optional outline argument is the color of
the rectangle’s outline.

*Ellipses
The ellipse(xy, fill, outline) method draws an ellipse. If the width
and height of the ellipse are identical, this method will draw a
circle. The xy argument is a box tuple (left, top, right, bottom) that
represents a box that precisely contains the ellipse. The optional
fill argument is the color of the inside of the ellipse, and the
optional outline argument is the color of the ellipse’s outline.

*Polygons
The polygon(xy, fill, outline) method draws an arbitrary polygon. The
xy argument is a list of tuples, such as [(x, y), (x, y), ...], or
integers, such as [x1, y1, x2, y2, ...], representing the connecting
points of the polygon’s sides. The last pair of coordinates will be
automatically connected to the first pair. The optional fill argument
is the color of the inside of the polygon, and the optional outline
argument is the color of the polygon’s outline.
"""