from . import screenTemplate

import pygame

import threading, asyncio

from ..UI import button, textBox, EditorItem, levelEditorScreen

from .. import globals, background

from ..RestAPI import imageRetriever


class ThemeSelector(screenTemplate.Screen):


    def __init__(self): 


        self.backButton.ChangePosition(5, 5)

        self.backButton.ChangeText('Back')


        self.submitButton.ChangePosition(globals.SCREEN_WIDTH / 2 - self.submitButton.getSize()[0] / 2, globals.SCREEN_HEIGHT / 1.5)

        self.submitButton.ChangeText('Submit')
        
        self.errorRect.center = (globals.SCREEN_WIDTH / 2, (globals.SCREEN_HEIGHT / 2) + 50)
        self.loadingRect.center = (globals.SCREEN_WIDTH / 2, (globals.SCREEN_HEIGHT / 2))


    def render(self, window):
        
        window.fill(self.background_colour)

        if (not self.loading):

            if (not self.editorMode):
                self.bg.Draw(window)
                self.submitButton.Draw(window)
                self.input.Draw(window)
                
            else:   
                self.editor.Draw(window)


            if (self.errorInput):
                window.blit(self.errorMessage, self.errorRect)

        else:
            window.fill((0,0,0))
            window.blit(self.loadingMessage, self.loadingRect)
            

   
        self.backButton.Draw(window)
            
    def Update(self, dt):
        self.editor.Update(dt)

        if (self.loading):
            print("loading")

    def processEvents(base, t_event):

        if (not base.loading):
            if (not base.editorMode):

                enterCheck = base.input.processEvents(t_event)

                submitCheck = base.submitButton.processEvents(t_event)

                if (base.errorInput and base.input.active):
                    base.errorInput = False

                if (enterCheck or submitCheck):
                    base.Load()

            else:
                editorCheck = base.editor.ProcessEvents(t_event, base.userInput)


            backCheck = base.backButton.processEvents(t_event)
            if (backCheck):
                base.ChangeMode(False)
                base.editor.ResetEditor()
                base.backButton.reset()
                return screenTemplate.Screens.MAIN_MENU

        return screenTemplate.Screens.MAIN_THEME_SELECTOR

        
    def ChangeMode(self, mode):
        #self.editor.editorMode = mode

        self.editorMode = mode

    def LoadingScreen(self):

        self.loading = True

        self.threadTracker.acquire()
        self.loading = False

        print("t2 done")

    def Load(self):
        
        t1 = threading.Thread(target=self.LoadProcess)
        t2 = threading.Thread(target=self.LoadingScreen)

        t1.start()
        t2.start()

    def LoadProcess(self):
        self.userInput = self.input.ReturnInput()
        valid = self.editor.RetrieveItemsAndBackground(self.userInput)

        if (valid):

            self.ChangeMode(True)

        else:
            self.errorInput = True

        self.threadTracker.release()
        #print("t1 done")
        


    backButton = button.Button()

    submitButton = button.Button()

    userInput = ""
    input = textBox.InputBox()
    imageGet = imageRetriever.imageController()
    editor = levelEditorScreen.EditorScreen()
    editorMode = False

    font = pygame.font.Font(None, 32)
    textColor = (255, 255, 255)
    errorMessage = font.render("Please choose a more appropriate key word.", True, textColor)
    errorRect = errorMessage.get_rect()
    errorInput = False

    threadTracker = threading.Semaphore(0)
    loading = False

    loadingFont = pygame.font.Font(None, 50)
    loadingMessage = loadingFont.render("Loading...", True, textColor)
    loadingRect = loadingMessage.get_rect()

    bg = background.image("../Assets/Leveleditor.jpg")