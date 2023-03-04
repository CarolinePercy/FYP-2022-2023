import pygame
import os

from ..UI import list, button, FindableItem, timer

from . import screenTemplate, levelEndScreen

from .. import globals, background


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Level(screenTemplate.Screen):

    def __init__(self):

        for i in self.items:

            self.gameList.AddToList(globals.g_itemTypes[i.thisType.value][3])


    def render(base, screen):

        screen.fill(base.background_colour)

        base.bg.Draw(screen)


        for i in base.items:

            i.Draw(screen)
        

        base.gameList.Draw(screen)

        base.time.Draw(screen)

        base.end.Draw(screen)
        

    def processEvents(base, t_event):   

        base.time.processEvents(t_event)
        
        for i in base.items:

            check = i.processEvents(t_event)


            if (check):

                base.items.remove(i)
                base.gameList.FoundItem(i.thisType)



        return screenTemplate.Screens.MAIN_GAME


    def update(base, dt):
        base.end.Update(dt)
        #base.time.Update(dt)

        if (base.gameList.DidPlayerFindAllItems()):
            timeLeft = base.time.StopTimer()
            base.end.EndLevel(timeLeft)

        

    background_colour = (100, 212, 12)

    screenRef = 0

    bg = background.image('../Assets/Library-Background.jpg')


    items = [

    FindableItem.FindableItem(globals.Item.WINE), 

    FindableItem.FindableItem(globals.Item.CLOCK),

    FindableItem.FindableItem(globals.Item.LAPTOP),

    FindableItem.FindableItem(globals.Item.BOOKS)

    ]


    gameList  = list.List()
    end = levelEndScreen.EndScreen()
    time = timer.Timer()
    