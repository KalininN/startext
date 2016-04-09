from math import *
from random import *

width = 2200
height = 1300

curtab = 0

def out(s):
    for i in range(curtab):
        print('  ', end='')
    print(s)

def pushgc():
    out('push graphic-context')
    global curtab
    curtab += 1

def popgc():
    global curtab
    curtab -= 1
    out('pop graphic-context')

npics = 5

def placerandom(x, y):
    out("image src-over %d,%d 30,30 'stars/star%d.svg'" % (x, y, randint(1, npics)))

pushgc()
out("viewbox 0 0 %d %d" % (width, height))
pushgc()
pushgc()
out("fill 'darkslateblue'")
out("stroke 'blue'")
out("stroke-width 1")
out("rectangle 0,0 %d,%d" % (width, height))
popgc()
pushgc()

step = 100
for x in range(width // step):
    placerandom(x * step, height // 2 + int(100 * sin(x / 3.0)))

popgc()
popgc()
popgc()