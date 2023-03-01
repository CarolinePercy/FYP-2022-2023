# import the pygame module
import pygame
#import numpy as np
import os

import Scripts.sceneManager as sceneManager
import Scripts.globals as globals
import Scripts.imageRetriever as imageRetriever

class main():
    
    def __init__(self):
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
        pygame.init()

    def processEvents(self, t_event):
        # Check for QUIT event    
        running = True

        if t_event.type == pygame.QUIT:
            running = False       

        self.gameController.processEvents(t_event)

        return running

    def update(self,dt):
        self.gameController.update(dt)

    def render(self):

        self.gameController.render(self.screen)   
        pygame.display.flip()
    

    # Set the caption of the screen
    pygame.display.set_caption('Hidden Object REST API Game!')
    gameController = sceneManager
    screen = 0
startGame = main()
# Variable to keep our game loop running
running = True

clock=pygame.time.Clock()

while running:  
# for loop through the event queue  
    dt = clock.tick(globals.FPS)
    for event in pygame.event.get():
            running = startGame.processEvents(event)
        
    
    startGame.update(dt)

    startGame.render()
    