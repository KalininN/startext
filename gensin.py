from math import *

from mvglib import *

width = 1000
height = 1000

img = StarPlacer(width, height)

step = 100
for x in range(width // step):
    img.placerandom(x * step, height // 2 + int(100 * sin(x / 3.0)))

img.generate_mvg('result.mvg')
