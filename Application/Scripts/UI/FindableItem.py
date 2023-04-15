import sys
from . import button

from ..RestAPI import imageRetriever
from .. import globals
import pygame



class FindableItem(button.Button):


    def __init__(self, path = "", t_distractor = False):
        # sets up the image itself

        self.distractor = t_distractor


        self.image = imageRetriever.imageController().getLocalImage(path)


#        self.image = pygame.transform.smoothscale(self.image, globals.g_itemTypes[path.value][1])


        self.image = self.image.convert_alpha()

        self.ChangeScale(self.image.get_width(), self.image.get_height())

#        self.ChangePosition(globals.g_itemTypes[path.value][2][0], globals.g_itemTypes[path.value][2][1])

        
    def Toggle(self, toggleValue):
        self.isActive = toggleValue
    

    def Draw(self, t_screen):
        if (self.isActive):
            t_screen.blit(self.image, (self.position[0], self.position[1]))
        
    isActive = True

    distractor = False
