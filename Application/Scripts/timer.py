import pygame

from . import globals
from . import imageRetriever
import time

class Timer():
    def __init__(self):
       self.StartTimer()

       self.timeAppearance = imageRetriever.imageController().getLocalImage("Assets/MainBox.png")
       self.timeAppearance = pygame.transform.smoothscale(self.timeAppearance, self.timeScale)

       self.timePlacement = ((globals.SCREEN_WIDTH / 2) - self.timeAppearance.get_width() / 2, 0);

       convertTime = time.strftime("%M:%S", time.gmtime(self.time))
       self.timeText = self.font.render(convertTime, True, self.text_color)

       self.textRect = self.timeText.get_rect()
       self.textRect.center = self.timeAppearance.get_rect().center
       self.textRect.centerx += self.timePlacement[0]


    def processEvents(base, t_event):
        if (t_event.type == pygame.USEREVENT):
            base.ReduceTime()

    def ReduceTime(self):
        if (self.stopTime == False):

            self.time -= 1
            convertTime = time.strftime("%M:%S", time.gmtime(self.time))

            self.timeText = self.font.render(convertTime, True, self.text_color)


        

    def Draw(self, t_screen):
        t_screen.blit(self.timeAppearance, self.timePlacement)
        t_screen.blit(self.timeText, self.textRect)

    
    def StartTimer(self):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        t = 0

    def StopTimer(self):
        self.stopTime = True
        return self.time

    clock = pygame.time.Clock()
    time = 300

    font = pygame.font.SysFont('franklingothicmedium', 18)
    text_color = (0, 0, 0)
    textRect = 0
    
    timeText = font.render('', True, text_color)
    timeAppearence = 0

    timePlacement = 0
    timeScale = (70, 40)
    stopTime = False