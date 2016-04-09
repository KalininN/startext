from random import *


class StarPlacer():
    def __init__(self, *args):
        self.width = int(args[0])
        self.height = int(args[1])
        self.stars = []
        self.npics = 6

    def __out(self, s):
        for i in range(self.curtab):
            print('  ', end='', file=self.file)
        print(s, file=self.file)

    def __pushgc(self):
        self.__out('push graphic-context')
        self.curtab += 1

    def __popgc(self):
        self.curtab -= 1
        self.__out('pop graphic-context')

    def placerandom(self, x, y):
        self.stars.append((x, y, randint(1, self.npics)))
    
    def generate_mvg(self, filename):
        with open(filename, "w") as self.file:
            self.curtab = 0
            self.__pushgc()
            self.__out("viewbox 0 0 %d %d" % (self.width, self.height))
            self.__pushgc()
            self.__pushgc()
            self.__out("fill 'darkslateblue'")
            self.__out("stroke 'blue'")
            self.__out("stroke-width 1")
            self.__out("rectangle 0,0 %d,%d" % (self.width, self.height))
            self.__popgc()
            self.__pushgc()
            for star in self.stars:
                self.__out("image src-over %d,%d 50,50 'stars/star%d.png'" % (star[0] - 25, star[1] - 25, star[2]))
            self.__popgc()
            self.__popgc()
            self.__popgc()
