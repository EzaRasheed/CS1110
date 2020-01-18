import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
bird = gamebox.from_image(100, 300, "http://cliparting.com/wp-content/uploads/2016/05/Blue-bird-clipart-2.png")
bird.scale_by(.08)

pillars = [
    gamebox.from_color(camera.y + 200, camera.bottom, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 350, camera.bottom, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 500, camera.bottom, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 650, camera.bottom, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 800, camera.bottom, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 950, camera.bottom, 'forest green', 40, random.randrange(100, 500)),

    gamebox.from_color(camera.y + 200, camera.top, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 350, camera.top, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 500, camera.top, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 650, camera.top, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 800, camera.top, 'forest green', 40, random.randrange(100, 500)),
    gamebox.from_color(camera.y + 950, camera.top, 'forest green', 40, random.randrange(100, 500)),
]

#game_on = False
ticks = 0
score = ticks


def tick(keys):
    #global game_on
    global score
    global ticks

    camera.clear('cyan')

    for pillar in pillars:
        camera.draw(pillar)

    # if pygame.K_SPACE in keys:
    #     game_on = True

    #if game_on is True:
    for pillar in pillars:
        pillar.speedx = -10
        pillar.move_speed()


    for pillar in pillars:
        if pygame.K_SPACE in keys:
            bird.speedy = -15
    bird.speedy *= 0.9
    bird.speedy += 2
    bird.move_speed()

    for pillar in pillars:
        pillar.x -= 3 #?
        if pillar.right < camera.left:
            pillar.x += 900
            pillar.size = (40, random.randrange(100, 550)) #?

    ticks += 1

    time = gamebox.from_text(0, 0, str(ticks//30), 'Arial', 40, 'black')
    time.touches = 700 #?
    time.top = camera.top
    time.right = camera.right
    camera.draw(time)

    scorer = gamebox.from_text(100, 60, 'Score: ' + str(ticks // 30), 'Arial', 30, 'red', bold=True)
    camera.draw(scorer)

    for pillar in pillars:
        bird.move_to_stop_overlapping(pillar, -50, -50)

    for pillar in pillars:
        if bird.touches(pillar, -13, -13):
            lose = gamebox.from_text(camera.x, camera.y, "You lost! You got " + str(ticks//30), 'Arial', 50, 'deep pink', bold=True)
            camera.draw(lose)
            gamebox.pause()

    if bird.x and bird.y > 800:
        lose = gamebox.from_text(camera.x, camera.y, "You lost! You got " + str(ticks//30), 'Arial', 50, 'deep pink', bold=True)
        camera.draw(lose)
        gamebox.pause()


    camera.draw(bird)
    camera.display()


ticks_per_second = 17
gamebox.timer_loop(ticks_per_second, tick)
