import pygame as pg

big_cactus = pg.image.load("assets/big_cactus.png")
#small = pg.image.load("assets/small_cactus.png")
#small_double = pg.image.load("assets/small_double_cactus.png")
#small_triple = pg.image.load("assets/small_triple_cactus.png")

class Cactus(object):
    def __init__(self, x, ground_y, velocity, size):
        self.x = x

        if size == 0:
        if size == 1:
        if size == 2:
        if size == 3:
        if size == 4:
        self.width = big_cactus.get_width()
        self.height = big_cactus.get_height()
        self.velocity = velocity
        self.size = size
        self.hitbox = (self.x, self.y, self.width, self.height)
        #TODO variable cactus sizes

    def draw(self, win):
        win.blit(big_cactus, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)


    def is_colliding(self, dino):
        if self.x < dino.get_Hx() + dino.get_Hwidth() and self.x + self.width > dino.get_Hx() and self.y < dino.get_Hy() + dino.get_Hheight() and self.y + self.height > dino.get_Hy():
            return True
        else:
            return False

    def draw_hitbox(self, win):
        pg.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height