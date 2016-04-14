from random import *
from subprocess import call


class StarPlacer():
    def __init__(self, *args):
        self.width = int(args[0])
        self.height = int(args[1])
        self.starsize = 50
        self.stars = []
        self.npics = 14

    def set_star_size(self, size):
        self.starsize = size

    def place_random(self, x, y):
        self.stars.append((x, y, randint(1, self.npics), randint(round(self.starsize * 0.7), round(self.starsize * 1.3)), randint(0, 11) * 32))

    def generate_mvg(self, filename):
        with open("mvglib.tmp", "w") as self.file:
            print("convert -size %dx%d xc:midnightblue \\" % (self.width, self.height), file=self.file)
            for star in self.stars:
                print("stars/star%d-rotated%d.png -geometry %dx%d+%d+%d -composite \\" %
                      (star[2], star[4], star[3], star[3], star[0] - star[3] / 2, star[1] - star[3] / 2), file=self.file)
            print(filename, file=self.file)

    def generate(self, filename):
        self.generate_mvg(filename)
        print("Preprocessing done, generating image...")
        call(["bash", "mvglib.tmp"])
