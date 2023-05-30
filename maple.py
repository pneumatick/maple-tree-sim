import random
from constants import MAP_WIDTH, MAP_HEIGHT

SEED_CYCLE = 75
MAX_SEEDS_PER_CYCLE = 15

class Maple:
    
    def __init__(self, age = 0, x = -1, y = -1):
        if x == -1: self.x = random.randint(0, MAP_WIDTH - 1)
        else: self.x = x
        if y == -1: self.y = random.randint(0, MAP_HEIGHT - 1)
        else: self.y = y
        self.health = random.randint(0, 100)
        self.age = age
        self.max_age = 500
        self.maturity = 100
        self.disp_rad = 15

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def increment_age(self):
        self.age += 1

    def cast_seed(self, num = 1):
        new_maples = []

        for i in range(random.randint(0, num)):
            x = random.randint(self.x - self.disp_rad, self.x + self.disp_rad)
            y = random.randint(self.y - self.disp_rad, self.y + self.disp_rad)

            if (x < 0):
                x = 0
            elif (x >= MAP_WIDTH):
                x = MAP_WIDTH - 1

            if (y < 0):
                y = 0
            elif (y >= MAP_HEIGHT):
                y = MAP_HEIGHT - 1

            new_maple = Maple(x = x, y = y)
            new_maples.append(new_maple)

        return new_maples
