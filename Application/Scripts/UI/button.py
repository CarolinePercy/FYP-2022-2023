import pygame

import sys

from ..RestAPI import imageRetriever


pygame.init()


class Button():

    def __init__(self, newSize = [140, 40], path = "buttonImage.png"):
        

        self.width = newSize[0]

        self.height = newSize[1]

        self.image = imageRetriever.imageController().getLocalImage("../Assets/" + path)


        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))


        self.image = self.image.convert_alpha()

        self.buttonRect = self.image.get_rect()


        self.darkerImage = self.image.copy()

        self.darkestImage = self.image.copy()


        darker = pygame.mask.from_surface(self.image)
        darker = darker.to_surface(setcolor=(1, 1, 1, .20 *255))
        darker.set_colorkey((0,0,0))

        darkest =pygame.mask.from_surface(self.image)
        darkest = darkest.to_surface(setcolor=(1, 1, 1, .40 *255))
        darkest.set_colorkey((0,0,0))

        self.darkerImage.blit(darker, (0, 0))
        self.darkestImage.blit(darkest, (0, 0))


        self.drawnImage = self.image    

    def ChangePosition(self, x, y):
        self.position = [x, y]
        self.UpdateRect()


    def ChangeScale(self, t_width, t_height):

        self.width = t_width
        self.height = t_height

        self.UpdateRect()
        self.UpdateText()

    def ChangeRotation(self, t_rotateBy):
        self.image = pygame.transform.rotate(self.image, t_rotateBy)
        self.darkerImage = pygame.transform.rotate(self.darkerImage, t_rotateBy)
        self.darkestImage = pygame.transform.rotate(self.darkestImage, t_rotateBy)
        self.drawnImage = pygame.transform.rotate(self.drawnImage, t_rotateBy)

        self.image.get_rect()

    def ChangeText(self, newText):  

        self.stringText = newText

        self.buttonText = self.font.render(self.stringText, True, self.text_color)

        self.UpdateText()


    def UpdateText(self):

        self.textRect = self.buttonText.get_rect()

        self.textRect.center = (self.position[0] + (self.width / 2), self.position[1] + (self.height / 2))


        reducer = 1


        tempFont = self.font


        while (self.textRect.width > self.width - 10):

            tempFont = pygame.font.SysFont(self.fontName, self.startFontSize - reducer)

            reducer += 1

            self.buttonText = tempFont.render(self.stringText, True, self.text_color)

            self.textRect = self.buttonText.get_rect()

            self.textRect.center = (self.position[0] + (self.width / 2), self.position[1] + (self.height / 2))


    def getSize(self):

        size = [self.width, self.height]

        return size


    def Hover(self, t_event):
        

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

            try:
                self.drawnImage = self.darkestImage
            except:
                None

            return True
        

        return False


    def Draw(self, t_screen):
        
        t_screen.blit(self.drawnImage, (self.position[0], self.position[1]))
        t_screen.blit(self.buttonText, self.textRect)

    def reset(self):
        self.drawnImage = self.image

    def processEvents(self, t_event):

        check = False


        if t_event.type == pygame.MOUSEBUTTONDOWN and t_event.button == 1: # 1 = left click in pygame

            check = self.Press()
        

        elif t_event.type == pygame.MOUSEMOTION or (t_event.type == pygame.MOUSEBUTTONUP and t_event.button == 1):

            self.Hover(t_event)
        

        return check

    def UpdateRect(self):
        self.buttonRect.update(self.position[0], self.position[1], 
        self.width, self.height)

    text_color = (0, 0, 0)

    stringText = ''


    width = 140

    height = 40

    position = [100, 20]

    buttonRect = pygame.rect.Rect(0, 0, 0, 0)


    image = 0

    darkerImage = 0

    drawnImage = 0


    startFontSize = 30

    fontName = 'twcen'

    font = pygame.font.SysFont(fontName, startFontSize)

    buttonText = font.render(stringText, True, text_color)

    textRect = buttonText.get_rect()

    textRect.center = (position[0] + (width / 2), position[1] + (height / 2))