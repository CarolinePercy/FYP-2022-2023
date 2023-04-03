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

        self.image[0].set_alpha(0)

    def render(self, window):
        
        window.fill(self.background_colour)

        window.blit(pygame.transform.scale(self.image[0], 
        (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)), (0, 0))

        self.backButton.Draw(window)
        self.submitButton.Draw(window)
        self.input.Draw(window)
        self.editor.Draw(window)
            
    def Update(self, dt):
        self.editor.Update(dt)

    def processEvents(base, t_event):
        backCheck = base.backButton.processEvents(t_event)

        enterCheck = base.input.processEvents(t_event)

        submitCheck = base.submitButton.processEvents(t_event)

        if (backCheck):
            return screenTemplate.Screens.MAIN_MENU

        if (enterCheck or submitCheck):
            userInput = base.input.ReturnInput()
            base.image = base.imageGet.RequestBackgrounds(userInput)
            base.editor.RetrieveItems(userInput)

            
        editerCheck = base.editor.ProcessEvents(t_event)
        
        return screenTemplate.Screens.MAIN_THEME_SELECTOR


    image = [pygame.Surface((0,0))]
    backButton = button.Button()
    submitButton = button.Button()
    input = textBox.InputBox()
    imageGet = imageRetriever.imageController()
    editor = levelEditorScreen.EditorScreen()
