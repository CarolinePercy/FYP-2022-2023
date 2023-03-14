from . import screenTemplate, mainMenu, mainGame, ThemeInputScreen, mainOptions
from ..RestAPI import imageRetriever

def __init__(self, screen):
    self.imageGet = imageRetriever.imageController().instance()
    #self.game = mainGame.Level()

def processEvents(t_event):
    global currentScreen
    
    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        currentScreen = menu.processEvents(t_event)

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        currentScreen = game.processEvents(t_event)
    
    elif (currentScreen == screenTemplate.Screens.MAIN_THEME_SELECTOR):
        currentScreen = themeSelector.processEvents(t_event)

    elif (currentScreen == screenTemplate.Screens.MAIN_OPTIONS):
        currentScreen = options.processEvents(t_event)

def render(screen):
    global currentScreen

    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        menu.render(screen)

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        game.render(screen)
    
    elif (currentScreen == screenTemplate.Screens.MAIN_THEME_SELECTOR):
        themeSelector.render(screen)

    elif (currentScreen == screenTemplate.Screens.MAIN_OPTIONS):
        options.render(screen)


def update(timePassed):
    global currentScreen

    if (currentScreen == screenTemplate.Screens.MAIN_MENU):
        None

    elif (currentScreen == screenTemplate.Screens.MAIN_GAME):
        game.update(timePassed)

    elif (currentScreen == screenTemplate.Screens.MAIN_THEME_SELECTOR):
        themeSelector.Update(timePassed)

    elif (currentScreen == screenTemplate.Screens.MAIN_OPTIONS):
        None

    imageGet.Update(timePassed)

currentScreen = screenTemplate.Screens.MAIN_MENU

game = mainGame.Level()
menu = mainMenu.Menu()
themeSelector = ThemeInputScreen.ThemeSelector()
options = mainOptions.Options()

imageGet = imageRetriever.imageController()