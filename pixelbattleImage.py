"""Main module"""

# = Import =

import PIL
from PIL import Image


# = Global Variables =

SizeX, SizeY = 10, 10
"""Size of the canvas"""

Canvas = Image.new(
    mode="RGB",
    size=(SizeX, SizeY),
    color=(255, 255, 255)
)
"""Global canvas"""

# = Functions =

def ClearCanvas():
    """Clear canvas"""
    global Canvas
    Canvas = Image.new(
        mode="RGB",
        size=(SizeX, SizeY),
        color=(255, 255, 255)
    )

def SetPixel(x:int, y:int, color:(int, int, int)):
    """Set one pixel"""
    global Canvas
    if (x < 0) or (y < 0) or (x >= SizeX) or (y >= SizeY):
        return
    Canvas.putpixel((x, y), color)

def Fill(x1:int, y1:int, x2:int, y2:int, color:(int, int, int)):
    """Fill rectangle"""
    global Canvas
    for x in range(x1, x2):
        for y in range(y1, y2):
            SetPixel(x, y, color)

def Show():
    """Show canvas"""
    global Canvas
    Canvas.show()
    # return Canvas