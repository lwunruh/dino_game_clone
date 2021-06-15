import pygame as pg

birdA = pg.image.load("assets/birdA.png")
birdB = pg.image.load("assets/birdB.png")

# for reference
crouchA = pg.image.load("assets/crouchA.png")

class Bird(object):
    def __init__(self, x, ground_y, velocity, elev):
        self.x = x
        if elev == 0:
            self.y = ground_y-birdA.get_height() - 5
        if elev == 1:
            self.y = ground_y-birdA.get_height()-crouchA.get_height() - 5
        if elev == 2:
            self.y = ground_y-birdA.get_height()-2*crouchA.get_height() - 5

        self.width = birdA.get_width()
        self.height = birdA.get_height()
        self.velocity = velocity
        self.elev = elev
        self.flap = 0

    def draw(self, win):

        if self.flap < 8 // 2:
            win.blit(birdA, (self.x, self.y))
        else:
            win.blit(birdB, (self.x, self.y))
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