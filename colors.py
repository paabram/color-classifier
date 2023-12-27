import model
import pygame as pg
from pygame.locals import * 
import random
import time
import sys

if __name__ == '__main__':
    # set up pygame and open the window
    pg.init()
    screen = pg.display.set_mode((800, 600), 0, 32)
    pg.display.set_caption('Colors')
    pg.display.toggle_fullscreen()

    # create text object
    font = pg.font.Font('freesansbold.ttf', 32)
    # and predictor object
    predictor = model.ColorPredictor()

    while 1:
        # check for quit
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            # allow escape key to exit fullscreen
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pg.display.toggle_fullscreen()
        
        # set a random color to fill the window
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        screen.fill(color)
        
        # have the predictor model name the color
        name = predictor.predict(color)
        # display the name in the center of the window
        text = font.render(name, True, (255, 255, 255))
        text_center = text.get_rect(center=(400, 300))
        screen.blit(text, text_center)

        pg.display.update()

        # leave this screen up for a second
        time.sleep(1)
