import pgzrun
import random

TITLE = "Pig Hunt"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3
pig.points = 0
pig.dead = False
pig.bot = False

beet = Actor("beetroot")
beet.x = 200
beet.y = 200


def draw():
    screen.blit("bg", (0, 0))
    beet.draw()
    pig.draw()
    screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
    if pig.dead:
        screen.draw.text(f"GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=70, color="#e30022",
                         fontname="kenney_bold")
        screen.draw.text(f"Press SPACE to try again", center=(WIDTH / 2, 2 * HEIGHT / 3), fontsize=30, color="#e30022",
                         fontname="kenney_bold")


def update():
    if pig.dead:
        return

    pig.x += pig.vx
    pig.y += pig.vy

    if pig.bot:
        bot()

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()

    if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
        pig.dead = True
        pig.x = WIDTH / 2
        pig.y = HEIGHT / 3
        pig.image = "pig_dead"


def bot():
    if pig.x - beet.x >= pig.v:
        on_key_down(keys.LEFT)
    elif beet.x - pig.x >= pig.v:
        on_key_down(keys.RIGHT)
    elif pig.y - beet.y >= pig.v:
        on_key_down(keys.UP)
    elif beet.y - pig.y >= pig.v:
        on_key_down(keys.DOWN)


def on_key_down(key):
    if pig.dead:
        if key == keys.SPACE:
            restart()

        return

    if key == keys.B:
        pig.bot = not pig.bot

    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


def restart():
    pig.image = "pig_down"
    pig.x = 400
    pig.y = 400
    pig.vx = 0
    pig.vy = 0
    pig.v = 3
    pig.points = 0
    pig.dead = False


pgzrun.go()
