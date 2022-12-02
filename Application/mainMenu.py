import screenTemplate
import pygame
import button
import globals

class Menu(screenTemplate.Screen):


    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2) - (self.startButton.width / 2)

        self.startButton.ChangePosition(centre, 200)

    # Methods
    def render(base, screen):
        screen.fill(base.background_colour)
        base.startButton.Draw(screen)

    def processEvents(base, t_event):   
        check = base.startButton.processEvents(t_event)

        if (check):
            return screenTemplate.Screens.MAIN_GAME
        
        return screenTemplate.Screens.MAIN_MENU

    startButton = button.Button()
    quitButton = button.Button()
    optionsButton = button.Button()
