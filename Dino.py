import pygame as pg

runA = pg.image.load("assets/runningA.png")
runB = pg.image.load("assets/runningB.png")
jump = pg.image.load("assets/neutral.png")
dead = pg.image.load("assets/dead.png")
crouchA = pg.image.load("assets/crouchA.png")
crouchB = pg.image.load("assets/crouchB.png")

class Dino(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJumping = False
        self.isCrouching = False
        self.walk = 0
        self.jumpCount = 10
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.isDead = False

    def draw(self, win):

        if self.isDead:
            win.blit(dead, (self.x, self.y))

        elif self.isCrouching:
            crouch_y = self.y + (runA.get_height() - crouchA.get_height())
            if self.walk < 8 // 2:
                win.blit(crouchA, (self.x, crouch_y))
            else:
                win.blit(crouchB, (self.x, crouch_y))

        elif self.isJumping:
            win.blit(jump, (self.x, self.y))

        else:
            if self.walk < 8 // 2:
                win.blit(runA, (self.x, self.y))
            else:
                win.blit(runB, (self.x, self.y))

        if self.isCrouching:
            self.hitbox = (self.x, self.y + (runA.get_height() - crouchA.get_height()), crouchA.get_width(), crouchA.get_height())
        else:
            self.hitbox = (self.x, self.y, self.width, self.height)

    def is_dead(self):
        return self.isDead

    def kill(self):
        self.isDead = True

    def draw_hitbox(self, win):
        pg.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def get_Hx(self):
        return self.hitbox[0]

    def get_Hy(self):
        return self.hitbox[1]

    def get_Hwidth(self):
        return self.hitbox[2]

    def get_Hheight(self):
        return self.hitbox[3]