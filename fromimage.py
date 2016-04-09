from random import *

from PIL import Image

from mvglib import StarPlacer

im = Image.open("text.png")

height = im.size[0]
width = im.size[1]
res = StarPlacer(height, width)


def getprob(whiteness):
    return (1 - whiteness) * 0.8 + 0.2


for i in range(5000):
    x = randint(25, height - 26)
    y = randint(25, width - 26)
    pixel = im.getpixel((x, y))
    whiteness = (pixel[0] + pixel[1] + pixel[2]) / (255 * 3)
    prob = getprob(whiteness)
    if random() < prob:
        res.placerandom(x, y)

res.generate_mvg('text.mvg')
