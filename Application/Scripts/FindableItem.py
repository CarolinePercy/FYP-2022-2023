import sys
from . import button

from . import imageRetriever
from . import globals
import pygame



class FindableItem(button.Button):


    def __init__(self, path, t_distractor = False):


        self.thisType = path

        # sets up the image itself

        self.distractor = t_distractor


        self.imp = imageRetriever.imageController().getLocalImage("Assets/" + globals.g_itemTypes[path.value][0])


        self.imp = pygame.transform.smoothscale(self.imp, globals.g_itemTypes[path.value][1])


        self.imp = self.imp.convert_alpha()


        self.ChangeScale(globals.g_itemTypes[path.value][1][0],globals.g_itemTypes[path.value][1][1])

        self.ChangePosition(globals.g_itemTypes[path.value][2][0], globals.g_itemTypes[path.value][2][1])

        

    

    def Draw(self, t_screen):

        #pygame.draw.rect(t_screen,self.pointerColour,self.buttonRect)

        t_screen.blit(self.imp, globals.g_itemTypes[self.thisType.value][2])
        
    

    distractor = False

    imp = 0

    thisType = 0

