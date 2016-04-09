from random import *

from PIL import Image

from mvglib import StarPlacer

im = Image.open("text.png")

height = im.size[0]
width = im.size[1]
res = StarPlacer(height, width)

starsize = 15
res.set_star_size(15)

def getprob(whiteness):
    return (1 - whiteness) * 0.95 + 0.05

points = []

for i in range(25000):
    x = randint(5, height - 6)
    y = randint(5, width - 6)
    pixel = im.getpixel((x, y))
    whiteness = (pixel[0] + pixel[1] + pixel[2]) / (255 * 3)
    prob = getprob(whiteness)
    if random() < prob:
        ok = True
        for p in points:
            if (x - p[0]) ** 2 + (y - p[1]) ** 2 < starsize ** 2 / 3.5:
                ok = False
        if not ok:
            continue
        points.append((x, y))
        res.place_random(x, y)

res.generate_mvg('text.mvg')
