from . import screenTemplate
import pygame
from ..UI import button
from .. import globals

class Menu(screenTemplate.Screen):


    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2) - (self.startButton.width / 2)

        self.startButton.ChangePosition(centre, 200)
        self.optionsButton.ChangePosition(centre, 300)
        self.quitButton.ChangePosition(centre, 400)

        self.startButton.ChangeText('Start')
        self.optionsButton.ChangeText('Options')
        self.quitButton.ChangeText('Quit')

    # Methods
    def render(base, screen):
        screen.fill(base.background_colour)
        base.startButton.Draw(screen)
        base.quitButton.Draw(screen)
        base.optionsButton.Draw(screen)

    def processEvents(base, t_event):   
        startCheck = base.startButton.processEvents(t_event)
        quitCheck = base.quitButton.processEvents(t_event)
        optionsCheck = base.optionsButton.processEvents(t_event)

        if (startCheck):
            return screenTemplate.Screens.MAIN_GAME
        elif(quitCheck):
            quit()
        elif(optionsCheck):
            return screenTemplate.Screens.MAIN_OPTIONS
        
        return screenTemplate.Screens.MAIN_MENU

    startButton = button.Button()
    quitButton = button.Button()
    optionsButton = button.Button()
