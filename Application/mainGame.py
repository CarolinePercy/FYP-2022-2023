import screenTemplate
import pygame
import button
import globals

class Level(screenTemplate.Screen):

    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2) - (self.button.width / 2)

        self.button.ChangePosition(centre, 200)
        self.button.ChangeText('Tests')


    # Methods
    def render(base, screen):
        screen.fill(base.background_colour)
        base.button.Draw(screen)

    def processEvents(base, t_event):   
        check = base.button.processEvents(t_event)

        return screenTemplate.Screens.MAIN_GAME

    button = button.Button()
    background_colour = (100, 212, 12)