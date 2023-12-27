import model
import pygame as pg
from pygame.locals import * 
import random
import time
import sys

# establish random initial color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color = [r, g, b]

# establish rate at which color changes (how much each frame max)
bound = 8

# establish rates that color makeup will shift at
# each of r/g/b will change by 1-10 in either direction every second, spin again if 0
r_rate = 0
g_rate = 0
b_rate = 0
rates = [r_rate, g_rate, b_rate]

def rate_randomize(i, direct = 'x'):
    # change one of the rates, bouncing to go in certain direction if necessary
    global rates

    if direct == '+':
        rates[i] = random.randint(1, bound)
    elif direct == '-':
        rates[i] = random.randint(-bound, -1)
    else:
        while rates[i] == 0:
            rates[i] = random.randint(-bound, bound)

for i in range(0,3):
    rate_randomize(i)

# set up window, fill it with the color
pg.init()
screen = pg.display.set_mode((800, 600), 0, 32)
pg.display.set_caption('Colors')

# pg.display.toggle_fullscreen()
pg.mouse.set_visible(False)

screen.fill(color)

predictor = model.ColorPredictor()
name = predictor.predict(color)

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render(name, False, (255, 255, 255), (0, 0, 0))

screen.blit(text, (0, 0))
pg.display.update()

while 1:
    # check for quit
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.display.toggle_fullscreen()
                if pg.mouse.get_visible():
                    pg.mouse.set_visible(False)
                else:
                    pg.mouse.set_visible(True)
            # change how quickly colors shift with a key press
            elif event.key == K_DOWN:
                if bound > 1:
                    bound -= 1
            elif event.key == K_UP:
                if bound < 20:
                    bound += 1
    
    # if any color would be out of bounds, change the rate to go in the opposite direction
    for i in range(0,3):
        if color[i] + rates[i] <= 0:
            rate_randomize(i, '+')
        elif color[i] + rates[i] >= 255:
            rate_randomize(i, '-')

    # update color
    for i in range(0,3):
        color[i] = color[i] + rates[i]
    
    # update screen
    screen.fill(color)
    name = predictor.predict(color)
    text = font.render(name, False, (255, 255, 255))

    screen.blit(text, (0, 0))
    pg.display.update()

    # sleep for 30 fps
    time.sleep(0.1)
