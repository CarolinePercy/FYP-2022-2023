from . import screenTemplate

import pygame

from ..UI import button

from .. import globals, background


class Menu(screenTemplate.Screen):

    def __init__(self):

        centre = (globals.SCREEN_WIDTH / 2) - (self.customLevelButton.width / 2)

        self.customLevelButton.ChangePosition(centre, 300)

        self.standardLevelButton.ChangePosition(centre, 400)

        self.quitButton.ChangePosition(centre, 500)

        self.customLevelButton.ChangeText('Create Level')

        self.standardLevelButton.ChangeText('Load Level')

        self.quitButton.ChangeText('Quit')

    def render(base, screen):

        screen.fill(base.background_colour)

        base.bg.Draw(screen)

        base.customLevelButton.Draw(screen)

        base.standardLevelButton.Draw(screen)

        base.quitButton.Draw(screen)

        screen.blit(base.bgText, base.textRect)

    def processEvents(base, t_event):   

        customCheck = base.customLevelButton.processEvents(t_event)

        standardCheck = base.standardLevelButton.processEvents(t_event)

        quitCheck = base.quitButton.processEvents(t_event)

        if (customCheck):
            base.customLevelButton.reset()
            return screenTemplate.Screens.MAIN_THEME_SELECTOR

        elif(quitCheck):
            quit()

        elif(standardCheck):
            base.standardLevelButton.reset()
            return screenTemplate.Screens.MAIN_GAME

        return screenTemplate.Screens.MAIN_MENU


    customLevelButton = button.Button()
    standardLevelButton = button.Button()
    quitButton = button.Button()

    bg = background.image("../Assets/MainMenu.jpg")
    bgFontName = 'inkfree'

    bgFont = pygame.font.SysFont(bgFontName, 90)

    bgText = bgFont.render("Hidden Art", True, (255, 219, 191))

    textRect = bgText.get_rect()

    textRect.center = (globals.SCREEN_WIDTH / 2, globals.SCREEN_HEIGHT / 5)

