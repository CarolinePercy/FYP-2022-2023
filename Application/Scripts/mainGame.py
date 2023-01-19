import pygame
import os

from . import list

from . import screenTemplate
from . import levelEndScreen

from . import button
from . import globals

from . import FindableItem

from . import background

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Level(screenTemplate.Screen):


    def __init__(self):

        #print(pygame.font.get_fonts())

        #centre = (globals.SCREEN_WIDTH / 2) - (self.button.width / 2)

        for i in self.items:

            self.gameList.AddToList(globals.g_itemTypes[i.thisType.value][3])
            print(globals.g_itemTypes[i.thisType.value][3])



    # Methods

    def render(base, screen):

        screen.fill(base.background_colour)

        base.bg.Draw(screen)


        for i in base.items:

            i.Draw(screen)
        

        base.gameList.Draw(screen)

        base.end.Draw(screen)
        


    def processEvents(base, t_event):   


        for i in base.items:

            check = i.processEvents(t_event)


            if (check):

                base.items.remove(i)
                base.gameList.FoundItem(i.thisType)



        return screenTemplate.Screens.MAIN_GAME


    background_colour = (100, 212, 12)

    screenRef = 0

    bg = background.image('Assets/Library-Background.jpg')


    items = [

    FindableItem.FindableItem(globals.Item.WINE), 

    FindableItem.FindableItem(globals.Item.CLOCK),

    FindableItem.FindableItem(globals.Item.LAPTOP),

    FindableItem.FindableItem(globals.Item.BOOKS)

    ]


    gameList  = list.List()
    end = levelEndScreen.EndScreen()
    