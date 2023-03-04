from . import screenTemplate
import pygame
from ..UI import button, textBox
from .. import globals
from ..RestAPI import imageRetriever

class ThemeSelector(screenTemplate.Screen):

    def __init__(self):

        self.backButton.ChangePosition(5, 5)
        self.backButton.ChangeText('Back')
        self.image.set_alpha(0)

    def render(self, window):
        
        window.fill(self.background_colour)

        window.blit(pygame.transform.scale(self.image, (1280, 720)), (0, 0))

        self.backButton.Draw(window)
        self.input.Draw(window)
            


    def processEvents(base, t_event):
        backCheck = base.backButton.processEvents(t_event)

        enterCheck = base.input.processEvents(t_event)

        submitCheck = base.submitButton.processEvents(t_event)

        if (backCheck):
            return screenTemplate.Screens.MAIN_MENU

        if (enterCheck or submitCheck):
            userInput = base.input.ReturnInput()
            base.image = base.imageGet.APIImageRequest(userInput)
            
            
        
        return screenTemplate.Screens.MAIN_THEME_SELECTOR


    image = pygame.Surface((0,0))
    backButton = button.Button()
    submitButton = button.Button()
    input = textBox.InputBox()
    imageGet = imageRetriever.imageController()
