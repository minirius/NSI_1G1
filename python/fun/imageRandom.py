# Imports PIL module
from PIL import Image
import random
import math
# creating a image object (new image object) with
# RGB mode and size 200x200
im = Image.new(mode="RGB", size=(1920, 1080))

def equ(x):
    return 10*x**2 + 5*x + 102

for i in range(1920):
    for j in range(1080):
        r = equ(i//(j+1))
        g = equ(i%(j+1))
        b = equ(int(j/(i+1)))
        im.putpixel((i, j), (r, g, b))
# This method will show image in any image viewer
im.show()