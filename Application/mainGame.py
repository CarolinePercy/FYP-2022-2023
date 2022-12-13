import screenTemplate
import pygame
import button
import globals
import FindableItem
import background
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Level(screenTemplate.Screen):

    def __init__(self):
        #centre = (globals.SCREEN_WIDTH / 2) - (self.button.width / 2)
        t = 0


    # Methods
    def render(base, screen):
        screen.fill(base.background_colour)
        base.bg.Draw(screen)
        base.item.Draw(screen)
        

    def processEvents(base, t_event):   
        check2 = base.item.processEvents(t_event)

        return screenTemplate.Screens.MAIN_GAME

    background_colour = (100, 212, 12)
    screenRef = 0
    bg = background.image('Assets/Library-Background.jpg')
    item = FindableItem.FindableItem(FindableItem.Item.WINE)