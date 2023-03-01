import pygame
import sys
from ..RestAPI import imageRetriever

pygame.init()

class Button():

    def __init__(self, path = "buttonImage.png"):
        t = 0
        self.image = imageRetriever.imageController().getLocalImage("../Assets/" + path)

        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

        self.image = self.image.convert_alpha()

        self.darkerImage = self.image.copy()
        self.darkestImage = self.image.copy()

        darker = pygame.Surface(self.image.get_size()).convert_alpha()
        darker.fill((0, 0, 0, .20 *255))
        self.darkerImage.blit(darker, (0, 0))

        self.drawnImage = self.image

    def ChangePosition(self, x, y):
        self.buttonRect = [x, y, self.width, self.height]
        self.position = [x, y]

    def ChangeScale(self, t_width, t_height):
        self.width = t_width
        self.height = t_height
        self.buttonRect = [self.position[0], self.position[1], t_width, t_height]

        self.UpdateText()

    def ChangeText(self, newText):
        self.buttonText = self.font.render(newText, True, self.text_color)
        self.UpdateText()

    def UpdateText(self):
        self.textRect = self.buttonText.get_rect()
        self.textRect.center = (self.position[0] + (self.width / 2), self.position[1] + (self.height / 2))

    def Hover(self):
        
        mouse = pygame.mouse.get_pos()

        left = self.position[0]
        right = self.width + self.position[0]
        top = self.position[1]
        bottom = self.height + self.position[1]

        if (left <= mouse[0] <= right and top <= mouse[1] <= bottom):
            self.drawnImage = self.darkerImage
        else:
            self.drawnImage = self.image

    def Press(self):

        mouse = pygame.mouse.get_pos()

        left = self.position[0]
        right = self.width + self.position[0]
        top = self.position[1]
        bottom = self.height + self.position[1]

        if (left <= mouse[0] <= right and top <= mouse[1] <= bottom):
            return True
        
        return False

    def Draw(self, t_screen):
        #pygame.draw.rect(t_screen,self.pointerColour,self.buttonRect)
        
        t_screen.blit(self.drawnImage, self.buttonRect)
        t_screen.blit(self.buttonText, self.textRect)

    def processEvents(self, t_event):
        check = False

        if t_event.type == pygame.MOUSEBUTTONDOWN:
            check = self.Press()
        
        if t_event.type == pygame.MOUSEMOTION or t_event.type == pygame.MOUSEBUTTONUP:
            self.Hover()
        
        return check

    text_color = (0, 0, 0)

    width = 140
    height = 40
    position = [100, 20]
    buttonRect = [position[0], position[1], width, height]

    image = 0
    darkerImage = 0
    drawnImage = 0

    font = pygame.font.SysFont('candara', 30)
    buttonText = font.render('Button', True, text_color)
    textRect = buttonText.get_rect()
    textRect.center = (position[0] + (width / 2), position[1] + (height / 2))