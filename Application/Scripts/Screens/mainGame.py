import pygame
import os

from ..UI import list, button, FindableItem, timer, levelEndScreen, textBox

from ..Saves import SaveReader

from . import screenTemplate

from .. import globals, background


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Level(screenTemplate.Screen):

    def __init__(self):

        #for i in self.items:

        #    self.gameList.AddToList(globals.g_itemTypes[i.thisType.value][3])

        self.submitButton.ChangePosition(globals.SCREEN_WIDTH / 2 - self.submitButton.getSize()[0] / 2, globals.SCREEN_HEIGHT / 1.5)

        self.submitButton.ChangeText('Submit')

    def render(base, screen):

        screen.fill(base.background_colour)

        if (base.levelSelected):
            try:
                base.bg.Draw(screen)   

            except:
                None

        if (base.gameIsActive):
            base.gameList.Draw(screen)

            base.time.Draw(screen)

        base.end.Draw(screen)

        if (not base.levelSelected):
            base.submitButton.Draw(screen)
            base.levelInput.Draw(screen)
        
    def processEvents(base, t_event):   

        base.time.processEvents(t_event)
        
        if (base.gameIsActive):
            base.gameList.ProcessEvents(t_event)

        else:
            retryCheck = base.end.ProcessEvents(t_event)

            if (retryCheck > 0):
                base.resetLevel()
                if (retryCheck == 2):
                    base.levelSelected = False
                    return screenTemplate.Screens.MAIN_MENU


        if (not base.levelSelected):
            enterCheck = base.levelInput.processEvents(t_event)

            submitCheck = base.submitButton.processEvents(t_event)

            if (enterCheck or submitCheck):
                base.saves.ReadDataFromJSON(base.levelInput.ReturnInput())
                base.gameList = base.saves.itemList
                base.bg = base.saves.background
                base.levelSelected = True
                base.gameIsActive = True
                base.time.StartTimer()

        return screenTemplate.Screens.MAIN_GAME

    def update(base, dt):
        base.end.Update(dt)
        #base.time.Update(dt)

        if (base.gameList.DidPlayerFindAllItems()):
            timeLeft = base.time.StopTimer()
            base.end.EndLevel(timeLeft)
            base.gameIsActive = False

    def resetLevel(self):
        #for i in self.items:
        #    i.Toggle(True)
            
        self.gameList.ResetList()
        self.gameIsActive = False
        self.levelSelected = False
        self.end.RestartLevel()
        self.time.StopTimer()

    screenRef = 0

    bg = ""

    gameIsActive = False
    levelSelected = False 

    gameList  = list.List()
    end = levelEndScreen.EndScreen()
    
    time = timer.Timer()
    levelInput = textBox.InputBox()
    submitButton = button.Button()
    saves = SaveReader.SaveStorer()