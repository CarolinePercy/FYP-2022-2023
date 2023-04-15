from . import screenTemplate

import pygame

from ..UI import button, textBox, EditorItem, levelEditorScreen

from .. import globals

from ..RestAPI import imageRetriever


class ThemeSelector(screenTemplate.Screen):


    def __init__(self):


        self.backButton.ChangePosition(5, 5)

        self.backButton.ChangeText('Back')


        self.submitButton.ChangePosition(globals.SCREEN_WIDTH / 2 - self.submitButton.getSize()[0] / 2, globals.SCREEN_HEIGHT / 1.5)

        self.submitButton.ChangeText('Submit')


    def render(self, window):
        
        window.fill(self.background_colour)

        if (not self.editorMode):
            self.submitButton.Draw(window)
            self.input.Draw(window)

        else:   
            self.editor.Draw(window)
   
        self.backButton.Draw(window)
            
    def Update(self, dt):
        self.editor.Update(dt)

    def processEvents(base, t_event):

        if (not base.editorMode):

            enterCheck = base.input.processEvents(t_event)

            submitCheck = base.submitButton.processEvents(t_event)

            if (enterCheck or submitCheck):
                userInput = base.input.ReturnInput()
                base.editor.RetrieveItemsAndBackground(userInput)
                base.ChangeMode(True)

        else:
            editorCheck = base.editor.ProcessEvents(t_event)


        backCheck = base.backButton.processEvents(t_event)
        if (backCheck):
            base.ChangeMode(False)
            base.editor.ResetEditor()
            return screenTemplate.Screens.MAIN_MENU

        return screenTemplate.Screens.MAIN_THEME_SELECTOR

        
    def ChangeMode(self, mode):
        #self.editor.editorMode = mode

        self.editorMode = mode


    backButton = button.Button()

    submitButton = button.Button()

    input = textBox.InputBox()
    imageGet = imageRetriever.imageController()
    editor = levelEditorScreen.EditorScreen()
    editorMode = False


