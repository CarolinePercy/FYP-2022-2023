from . import screenTemplate
import pygame
from . import button
from . import textBox
from . import globals

class Options(screenTemplate.Screen):

    def __init__(self):

        self.backButton.ChangePosition(5, 5)
        self.backButton.ChangeText('Back')

    def render(self, window):
        window.fill(self.background_colour)
        self.backButton.Draw(window)
        self.input.Draw(window)

    def processEvents(base, t_event):
        backCheck = base.backButton.processEvents(t_event)

        base.input.processEvents(t_event)

        if (backCheck):
            return screenTemplate.Screens.MAIN_MENU
        
        return screenTemplate.Screens.MAIN_OPTIONS



    backButton = button.Button()
    submitButton = button.Button()
    input = textBox.InputBox()
