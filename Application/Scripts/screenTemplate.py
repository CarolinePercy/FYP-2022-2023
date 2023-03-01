import pygame
import sys
from enum import Enum

class Screens(Enum):
    MAIN_MENU = 0
    MAIN_GAME = 1
    MAIN_OPTIONS = 2

class Screen():

    #Methods
    def processEvents(self, event):
        if t_event.type == pygame.MOUSEBUTTONDOWN:
            t = 0
    
    def render(self, window):
        screen.fill(self.background_colour)

    # Variables
    background_colour = (234, 212, 252)