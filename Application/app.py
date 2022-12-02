# import the pygame module
import pygame
import numpy as np
import sceneManager

import globals
import imageRetriever

def processEvents(t_event):
    # Check for QUIT event    
    running = True

    if t_event.type == pygame.QUIT:
        running = False       

    gameController.processEvents(t_event)

    return running

def render():

    gameController.render(screen)
    
    #screen.blit(image, (100, 100))    

    # Update the display using flip
    pygame.display.flip()
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
  
# Set the caption of the screen
pygame.display.set_caption('Hidden Object REST API Game!')

#img = imageRetriever.imageController()

#image = pygame.image.load(img.getImage())

gameController = sceneManager

# Variable to keep our game loop running
running = True
  
while running:  
# for loop through the event queue  
    for event in pygame.event.get():
        
        running = processEvents(event)

    render()