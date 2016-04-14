from random import *
import argparse

from PIL import Image

from mvglib import StarPlacer

parser = argparse.ArgumentParser(description='Make picture with stars arranged to form the picture.')
parser.add_argument('inputfile', metavar='input',
                   help='an input picture')
parser.add_argument('outputfile', metavar='output',
                   help='an output picture')

args = parser.parse_args()

im = Image.open(args.inputfile)

height = im.size[0]
width = im.size[1]
res = StarPlacer(height, width)

starsize = round((width + height) * 0.008)
res.set_star_size(starsize)

def getprob(whiteness):
    return (1 - whiteness) * 0.97 + 0.03

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

res.generate(args.outputfile)
