import pygame

from .. import globals
from ..RestAPI import imageRetriever

from . import button
import time

class EndScreen():

    def __init__(self):
        self.titleBox = imageRetriever.imageController().getLocalImage("../Assets/TitleBox.png")
        self.mainBox = imageRetriever.imageController().getLocalImage("../Assets/MainBox.png")

        self.titleBox = pygame.transform.smoothscale(self.titleBox, self.titleScale)
        self.mainBox = pygame.transform.smoothscale(self.mainBox, self.mainScale)

        self.titlePlace = ((globals.SCREEN_WIDTH / 2) - self.titleBox.get_width() / 2, 
        (globals.SCREEN_HEIGHT / 3) - self.titleBox.get_height() / 2)

        self.mainPlace = ((globals.SCREEN_WIDTH / 2) - self.mainBox.get_width() / 2,
        (globals.SCREEN_HEIGHT / 1.8) - self.mainBox.get_height() / 2)

        self.transparentSurface.set_alpha(self.alpha)
        self.transparentSurface.fill((0,0,0))

        self.redoButton.ChangePosition(self.mainPlace[0],  self.mainPlace[1] + self.mainBox.get_height())
        self.exitButton.ChangePosition(self.mainPlace[0] + self.mainBox.get_width() - self.exitButton.getSize()[0],  self.mainPlace[1] + self.mainBox.get_height())


    def Draw(self, t_screen):

        if (self.finished):
            t_screen.blit(self.transparentSurface, (0,0))

            t_screen.blit(self.mainBox, self.mainPlace)
            t_screen.blit(self.titleBox, self.titlePlace)

            t_screen.blit(self.textObject, self.textRect.center)

            self.redoButton.Draw(t_screen)
            self.exitButton.Draw(t_screen)

    def Update(self, dt):

        if (self.finished):

            if (self.finalAlpha > self.alpha):
                self.alpha += 4

            self.transparentSurface.set_alpha(self.alpha)

    def ProcessEvents(self, t_event):
        if (self.finished):
            retryCheck = self.redoButton.processEvents(t_event)
            exitCheck = self.exitButton.processEvents(t_event)

            if (retryCheck):
                None
                return 1

            if (exitCheck):
                None
                return 2
        
        return 0
    
    def EndLevel(self, timeLeft):

        self.finished = True
        convertTime = time.strftime("%M:%S", time.gmtime(timeLeft))
        timeText = "Time - " + str(convertTime)

        self.textObject = self.font.render(timeText, True, self.text_color)
        self.textRect = self.textObject.get_rect()

        self.textRect.center = ((globals.SCREEN_WIDTH / 2) - self.textRect.width / 2, 
        (globals.SCREEN_HEIGHT / 2) - self.textRect.height / 2)

    def RestartLevel(self):
        self.finished = False
        self.alpha = 0
        self.transparentSurface.set_alpha(self.alpha)

    completedLevel = False

    font = pygame.font.SysFont('franklingothicmedium', 18)

    titleBox = 0
    mainBox = 0

    titlePlace = 0
    mainPlace = 0
    titleScale = (291, 65)#291 : 65
    mainScale = (384,236) #96 : 59

    score = 0
    scoreText = ""

    text_color = (0, 0, 0)
    textObject = ""

    textRect = font.render('', True, text_color)

    redoButton = button.Button((49,33),"RetryButton.png")
    exitButton = button.Button((49, 33), "CloseButton.png")

    transparentSurface = pygame.Surface((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
    alpha = 0
    finalAlpha = 180
    finished = False
    
     