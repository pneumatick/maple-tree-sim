import random
from constants import *

class Squirrel:

    def __init__(self, x = -1, y = -1):
        if x == -1: self.x = random.randint(0, MAP_WIDTH - 1)
        else: self.x = x
        if y == -1: self.y = random.randint(0, MAP_HEIGHT - 1)
        else: self.y = y
        self.health = random.randint(0, 25)
        self.energy = 0
        self.age = 0
        self.max_age = 200

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def increment_age(self):
        self.age += 1

    def increment_energy(self):
        self.energy += 1

    def reset_energy(self):
        self.energy = 0

    def reproduce(self, num = random.randint(0, 4)):
        new_squirrels = []

        for i in range(num):
            x = random.randint(self.x - 10, self.x + 10)
            y = random.randint(self.y - 10, self.y + 10)

            if (x < 0):
                x = 0
            elif (x >= MAP_WIDTH):
                x = MAP_WIDTH - 1

            if (y < 0):
                y = 0
            elif (y >= MAP_HEIGHT):
                y = MAP_HEIGHT - 1

            new_squirrel = Squirrel(x = x, y = y)
            new_squirrels.append(new_squirrel)

        return new_squirrels
