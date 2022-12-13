import sys
import button
import imageRetriever
import pygame
from enum import Enum

class Item(Enum):
    WINE = 0
    CLOCK = 1
    LAPTOP = 2
    BOOKS = 3

class FindableItem(button.Button):

    def __init__(self, path, t_distractor = False):

        thisType = path
        # sets up the image itself
        self.distractor = t_distractor

        self.imp = imageRetriever.imageController().getLocalImage("Assets/" + self.itemTypes[path.value][0])

        self.imp = pygame.transform.smoothscale(self.imp, self.itemTypes[path.value][1])

        self.imp = self.imp.convert_alpha()

        self.imp.set_colorkey((0, 0, 0))

        pygame.Surface.convert_alpha(self.imp)

        self.ChangeScale(self.itemTypes[path.value][1][0],self.itemTypes[path.value][1][1])
        self.ChangePosition(self.itemTypes[path.value][2][0], self.itemTypes[path.value][2][1])

        

    
    def Draw(self, t_screen):
        pygame.draw.rect(t_screen,self.pointerColour,self.buttonRect)
        t_screen.blit(self.imp, self.itemTypes[self.thisType][2])
        

    #def ScaleImage(self, type):
        #pygame.transform.scale(self.imp, (100, 100))


    
    itemTypes = [["GlassOfWine.png", (25, 60),(510,360)],["Clock.png", (200, 200),(0,0)]]
    
    distractor = False
    imp = 0
    thisType = 0
