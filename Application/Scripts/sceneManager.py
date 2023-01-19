from . import screenTemplate

from . import mainMenu
from . import mainGame

def __init__(self, screen):
    self.game = mainGame.Level()

def processEvents(t_event):
    global currentScreen

    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        currentScreen = menu.processEvents(t_event)

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        currentScreen = game.processEvents(t_event)

def render(screen):
    global currentScreen

    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        menu.render(screen)

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        game.render(screen)

def update(timePassed):
    global currentScreen

    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        #menu.render(screen)
        t = 0

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        game.update(timePassed)

currentScreen = screenTemplate.Screens.MAIN_MENU

game = mainGame.Level()
menu = mainMenu.Menu()