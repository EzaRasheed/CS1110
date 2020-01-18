import pygame
import gamebox
import random

"""
Our game is going to be a running game in which the dog has to jump onto stairs in order to survive. The stairs are in different heights, and are moving towards the dog. 
If the dog misses the staircases and falls, the game would end and the timer will display the score. There are enemies and collectibles in this game. If the dog 
touches the enemies, its health meter level will drop. If the dog touches the collectibles, its health meter level will rise. There are two ways to die:
one is when the dog's health meter runs out, and the other is when it falls.
For our optional features, we will have collectibles, enemies, health meter, and sound effects"""

camera = gamebox.Camera(800, 600)
wall1 = gamebox.from_color(random.randrange(0, 800), 150, 'black', random.randrange(400, 500), 10)
wall2 = gamebox.from_color(random.randrange(0, 800), 300, 'black', random.randrange(400, 500), 10)
wall3 = gamebox.from_color(random.randrange(0, 800), 450, 'black', random.randrange(400, 500), 10)
wall4 = gamebox.from_color(random.randrange(800, 1600), 150, 'black', random.randrange(400, 500), 10)
wall5 = gamebox.from_color(random.randrange(800, 1600), 300, 'black', random.randrange(400, 500), 10)
wall6 = gamebox.from_color(random.randrange(800, 1600), 450, 'black', random.randrange(400, 500), 10)
#the walls are the moving stairs and there will be three levels for their heights

wall7 = gamebox.from_color(400, 600, 'red', 800, 10) #the 'lava'
walls = [wall1, wall2, wall3, wall4, wall5, wall6]

start = gamebox.from_text(400, 200, 'Doggy Run!', 'Arial', 80, 'blue')
names = gamebox.from_text(400, 300, 'Caroline Li, pl5bx | Eza Rasheed, er6qt', 'Arial', 30, 'purple')
instructions = gamebox.from_text(400, 400, 'Press spacebar to start ', 'Arial', 30, 'blue')
instructions2 = gamebox.from_text(400, 500 , 'Press spacebar to jump, Press B for a booster jump ', 'Arial', 30, 'blue')
startscreen = [start, names, instructions, instructions2] #this is our startscreen

dog = gamebox.from_image(300, 200, 'http://www.joggydoggy.co.uk/communities/7/004/013/190/367//images/4622606177_306x228.png')
dog.scale_by(.6)

enemy = gamebox.from_image(750, 300, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Twemoji_1f47e.svg/768px-Twemoji_1f47e.svg.png')
enemy.scale_by(.08)

game_on = False

treat = [] #collectables
for i in range(5):
    t = gamebox.from_image(random.randrange(0, 800), random.randrange(0, 600), 'http://cliparting.com/wp-content/uploads/2017/07/Dog-bone-clipart-3.png')
    t.scale_by(0.1)
    treat.append(t)

dog.timer = 16
def tick(keys):
    global game_on

    camera.clear('lightcoral')


    camera.draw(wall7)

    for wall in walls:
        camera.draw(wall)

    if pygame.K_SPACE in keys: #user input starts the game
        game_on = True
    if game_on == True:
        for wall in walls:
            wall.speedx = -10 #walls moving in constant speed
            wall.move_speed()

        for wall in walls:
            if wall.right < camera.left: #walls locations change as we recycle them
                wall.left += 1200
                wall.size = random.randrange(300, 400), 10


        # camera.draw(dog)
        # if enemy.x < dog.x:
        #     enemy.speedx += 1
        # if enemy.x > dog.x:
        #     enemy.speedx -= 1
        # if enemy.y < dog.y:
        #     enemy.speedy += 1
        # if enemy.y > dog.y:
        #     enemy.speedy -= 1
        #     # drag
        # enemy.speedx *= 0.95
        # enemy.speedy *= 0.95
        # # momentum
        # enemy.move_speed()

        camera.draw(enemy)
        for wall in walls:
            if dog.bottom_touches(wall): #jumping only when on stair, cannot jump out of thin air
                if pygame.K_SPACE in keys:
                    dog.speedy = -20
        dog.speedy *= 0.9 #gravity effects
        dog.speedy += 1
        dog.move_speed()

        for wall in walls:
            if enemy.bottom_touches(wall):
                    enemy.speedy = -1
        enemy.speedy *= 0.9  # gravity effects
        enemy.speedy += 1
        enemy.move_speed()

        for wall in walls:
            if dog.bottom_touches(wall):  # dog cannot fall through stair
                dog.speedx = 0
            dog.move_to_stop_overlapping(wall, -40, -40)

        for wall in walls:
            if enemy.bottom_touches(wall):  # enemy cannot fall through stair
                enemy.speedx = 0
            enemy.move_to_stop_overlapping(wall, -40, -40)

        for coin in treat:
            camera.draw(coin)
            coin.speedx = -10
            coin.move_speed()
        for coin in treat:
            if coin.x < 0:
                coin.x = random.randrange(800, 1600)
        for coin in treat:
            if dog.touches(coin, -60, -60):
                coin.x = random.randrange(800, 1600)
                #health level +1
                #play sound



        # if dog.touches(wall7, -60, -60): #game over
        #     game_over = gamebox.from_text(camera.x, camera.y, 'Game Over!', 'Arial', 100, 'black', bold=True)
        #     camera.draw(game_over)
        #     gamebox.pause()
    if game_on == False:
        for thing in startscreen:
            camera.draw(thing)
    camera.display()


gamebox.timer_loop(30, tick)

