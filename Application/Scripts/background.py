from .RestAPI import imageRetriever
from . import globals
import pygame
class image:

    def __init__(self, path):
        self.imp = imageRetriever.imageController().getLocalImage(path)

        
    
    def Draw(self, t_screen):
        t_screen.blit(pygame.transform.scale(self.imp, (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)), (0, 0))