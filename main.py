import pygame as pg
import Cactus
import Dino
import Bird
import random as r

pg.init()

winx = 700
winy = 250
ground_y = winy-50
win = pg.display.set_mode((winx, winy))
pg.display.set_caption("The Dino Game")

clock = pg.time.Clock()

#Size references
runA = pg.image.load("assets/runningA.png")
big_cactus = pg.image.load("assets/big_cactus.png")

restart = pg.image.load("assets/restart.png")
game_over = pg.image.load("assets/game_over.png")


def redraw_window():
    win.fill((0, 0, 0))
    dino.draw(win)
    #dino.draw_hitbox(win)

    for cactus in cacti:
        cactus.draw(win)
        #cactus.draw_hitbox(win)

    for bird in birds:
        bird.draw(win)
        #bird.draw_hitbox(win)

    pg.draw.rect(win, (255, 255, 255), (0, ground_y, winx, 3))
    pg.display.update()


def walk_step(dino):
    if dino.walk == 8:
        dino.walk = 0
    else:
        dino.walk += 1

def flap(bird):
    if bird.flap == 8:
        bird.flap = 0
    else:
        bird.flap += 1

def release_cactus():
    cacti.append(Cactus.Cactus(winx, ground_y, enemy_v, r.randrange(0, 5)))

def release_bird():
    birds.append(Bird.Bird(winx, ground_y, enemy_v, r.randrange(0, 3)))


def restart_game():
    global dino
    global cacti
    global enemyCount
    global birds
    global enemy_v
    global v_count
    global running

    dino = Dino.Dino(winx/6-runA.get_width(), ground_y - runA.get_height(), runA.get_width(), runA.get_height())
    cacti = []
    enemyCount = 50
    birds = []
    enemy_v = 10
    v_count = 0
    running = True

restart_game()

while running:
    clock.tick(30)

    #Slowly increase game speed
    if v_count == 300:
        v_count = 0
        enemy_v += 1
    else:
        v_count += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # No clue what's going on here, it just kinda works
    walk_step(dino)

    keys = pg.key.get_pressed()
    # Movement stuff
    if keys[pg.K_SPACE] or keys[pg.K_UP]:
        dino.isJumping = True
    if keys[pg.KMOD_SHIFT] or keys[pg.K_DOWN]:
        dino.isCrouching = True
    else:
        dino.isCrouching = False
    # Jumping formula
    if dino.isJumping:
        if dino.jumpCount >= -10:
            neg = 1
            if dino.jumpCount < 0:
                neg = -1
            dino.y -= (dino.jumpCount/2)**2 * neg
            dino.jumpCount -= 1
        else:
            dino.isJumping = False
            dino.jumpCount = 10


    # Cactus stuff
    for cactus in cacti:
        if cactus.x + cactus.get_width() >= 0:
            cactus.x -= cactus.velocity
        else:
            cacti.remove(cactus)

        if cactus.is_colliding(dino):
            dino.kill()

    # Bird stuff
    for bird in birds:
        if bird.get_x() + bird.get_width() >= 0:
            bird.x -= bird.velocity
        else:
            birds.remove(bird)

        if bird.is_colliding(dino):
            dino.kill()

        flap(bird)

    # Periodically release an enemy
    if enemyCount == 100:
        if r.randrange(0, 10) > 2:
            release_cactus()
        else:
            release_bird()
        enemyCount = int(r.choice((10, 20, 40, 50, 60, 70)))
    else:
        enemyCount += 1



    #Death stuff
    if dino.is_dead():
        redraw_window()
        while(running):
            go_x = winx/2 - game_over.get_width()/2
            res_x = winx/2 - restart.get_width()/2

            win.blit(game_over, (go_x, winy/3))
            res = win.blit(restart, (res_x, winy/3 + game_over.get_height() + 10))
            pg.display.update()

            restartflag = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    if res.collidepoint(a, b):
                        restart_game()
                        restartflag = True

            if restartflag:
                break

    redraw_window()

print("GAME OVER")

pg.quit()
