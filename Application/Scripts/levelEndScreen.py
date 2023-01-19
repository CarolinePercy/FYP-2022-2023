import pygame

from . import globals
from . import imageRetriever

from . import button

class EndScreen():

    def __init__(self):
        self.titleBox = imageRetriever.imageController().getLocalImage("Assets/TitleBox.png")
        self.mainBox = imageRetriever.imageController().getLocalImage("Assets/MainBox.png")

        self.titleBox = pygame.transform.smoothscale(self.titleBox, self.titleScale)
        self.mainBox = pygame.transform.smoothscale(self.mainBox, self.mainScale)

        self.titlePlace = ((globals.SCREEN_WIDTH / 2) - self.titleBox.get_width() / 2, 
        (globals.SCREEN_HEIGHT / 3) - self.titleBox.get_height() / 2)

        self.mainPlace = ((globals.SCREEN_WIDTH / 2) - self.mainBox.get_width() / 2,
        (globals.SCREEN_HEIGHT / 1.8) - self.mainBox.get_height() / 2)

        self.transparentSurface.set_alpha(self.alpha)
        self.transparentSurface.fill((0,0,0))


    def Draw(self, t_screen):

        if (self.finished):
            t_screen.blit(self.transparentSurface, (0,0))

            t_screen.blit(self.mainBox, self.mainPlace)
            t_screen.blit(self.titleBox, self.titlePlace)

    def Update(self, dt):

        if (self.finished):

            if (self.finalAlpha > self.alpha):
                self.alpha += 4

            self.transparentSurface.set_alpha(self.alpha)
    
    def EndLevel(self):
        self.finished = True

    titleBox = 0
    mainBox = 0

    completedLevel = False

    font = pygame.font.SysFont('franklingothicmedium', 18)

    titlePlace = 0
    mainPlace = 0
    titleScale = (291, 65)#291 : 65
    mainScale = (384,236) #96 : 59
    finalStop = [0, 0]

    transparentSurface = pygame.Surface((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
    alpha = 0
    finalAlpha = 180
    finished = False
    
     