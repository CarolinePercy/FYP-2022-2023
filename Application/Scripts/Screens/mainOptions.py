from . import screenTemplate
import pygame
from ..UI import button
from .. import globals

class Options(screenTemplate.Screen):

    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2) - (self.backButton.width / 2)

        self.backButton.ChangePosition(centre, 400)

        self.backButton.ChangeText('Back')


    def render(base, screen):
        screen.fill(base.background_colour)
        base.backButton.Draw(screen)

    def processEvents(base, t_event):   
        backCheck = base.backButton.processEvents(t_event)

        if(backCheck):
            return screenTemplate.Screens.MAIN_MENU
        
        return screenTemplate.Screens.MAIN_OPTIONS

    backButton = button.Button()
