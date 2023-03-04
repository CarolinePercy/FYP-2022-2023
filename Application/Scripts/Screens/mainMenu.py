from . import screenTemplate

import pygame

from ..UI import button

from .. import globals


class Menu(screenTemplate.Screen):

    def __init__(self):

        centre = (globals.SCREEN_WIDTH / 2) - (self.customLevelButton.width / 2)

        self.customLevelButton.ChangePosition(centre, 200)

        self.standardLevelButton.ChangePosition(centre, 300)

        self.optionsButton.ChangePosition(centre, 400)

        self.quitButton.ChangePosition(centre, 500)

        self.customLevelButton.ChangeText('Custom Level')

        self.standardLevelButton.ChangeText('Standard Level')

        self.optionsButton.ChangeText('Options')

        self.quitButton.ChangeText('Quit')

    def render(base, screen):

        screen.fill(base.background_colour)

        base.customLevelButton.Draw(screen)

        base.standardLevelButton.Draw(screen)

        base.quitButton.Draw(screen)

        base.optionsButton.Draw(screen)

    def processEvents(base, t_event):   

        customCheck = base.customLevelButton.processEvents(t_event)

        standardCheck = base.standardLevelButton.processEvents(t_event)

        quitCheck = base.quitButton.processEvents(t_event)

        optionsCheck = base.optionsButton.processEvents(t_event)

        if (customCheck):
            return screenTemplate.Screens.MAIN_THEME_SELECTOR

        elif(quitCheck):
            quit()

        elif(standardCheck):
            return screenTemplate.Screens.MAIN_GAME

        elif(optionsCheck):
            return screenTemplate.Screens.MAIN_OPTIONS

        return screenTemplate.Screens.MAIN_MENU


    customLevelButton = button.Button()
    standardLevelButton = button.Button()
    quitButton = button.Button()
    optionsButton = button.Button()


