from random import *


class StarPlacer():
    def __init__(self, *args):
        self.width = int(args[0])
        self.height = int(args[1])
        self.starsize = 50
        self.stars = []
        self.npics = 6

    def set_star_size(self, size):
        self.starsize = size

    def place_random(self, x, y):
        self.stars.append((x, y, randint(1, self.npics)))
    
    def generate_mvg(self, filename):
        with open(filename, "w") as self.file:
            print("convert -size %dx%d xc:darkslateblue \\" % (self.width, self.height), file=self.file)
            for star in self.stars:
                print("stars/star%d.png -geometry %dx%d+%d+%d -composite \\" %
                      (star[2], self.starsize, self.starsize, star[0] - self.starsize / 2, star[1] - self.starsize / 2), file=self.file)
            print("result.png", file=self.file)
