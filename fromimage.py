from random import *

from PIL import Image

from mvglib import StarPlacer

im = Image.open("text.png")

height = im.size[0]
width = im.size[1]
res = StarPlacer(height, width)
res.set_star_size(10)

def getprob(whiteness):
    return (1 - whiteness) * 0.8 + 0.2


for i in range(10000):
    x = randint(5, height - 6)
    y = randint(5, width - 6)
    pixel = im.getpixel((x, y))
    whiteness = (pixel[0] + pixel[1] + pixel[2]) / (255 * 3)
    prob = getprob(whiteness)
    if random() < prob:
        res.place_random(x, y)

res.generate_mvg('text.mvg')
