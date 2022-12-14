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

        self.thisType = path
        # sets up the image itself
        self.distractor = t_distractor

        self.imp = imageRetriever.imageController().getLocalImage("Assets/" + self.itemTypes[path.value][0])

        self.imp = pygame.transform.smoothscale(self.imp, self.itemTypes[path.value][1])

        self.imp = self.imp.convert_alpha()

        self.ChangeScale(self.itemTypes[path.value][1][0],self.itemTypes[path.value][1][1])
        self.ChangePosition(self.itemTypes[path.value][2][0], self.itemTypes[path.value][2][1])

        

    
    def Draw(self, t_screen):
        #pygame.draw.rect(t_screen,self.pointerColour,self.buttonRect)
        t_screen.blit(self.imp, self.itemTypes[self.thisType.value][2])
        

    itemTypes = [["GlassOfWine.png", (25, 60),(510,360)],
    ["Clock.png", (50, 50),(397,155)],
    ["Laptop.png", (200, 100),(200,600)],
    ["StackOfBooks.png", (80, 80),(820,430)]]
    
    distractor = False
    imp = 0
    thisType = 0
