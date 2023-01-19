import pygame

from . import globals
from . import imageRetriever

class List():

    def __init__(self):
        self.listAppearance = imageRetriever.imageController().getLocalImage("Assets/ListAppearance.png")

    def AddToList(self, item):
        self.objectList.append([item, False])

    def FoundItem(self, item):

        index = 0
        for type in globals.Item:

            if (item == type):        
                self.objectList[index][1] = True
                
            index += 1

    def Draw(self, t_screen):
        t_screen.blit(self.listAppearance, self.listPlacement)
        placement = 1

        for item in self.objectList:

            if (item[1]):
                
                self.font.set_underline(False)
                self.font.set_bold(False)
                
                self.objectText = self.font.render(item[0], True, self.cross_out_colour)

            else:
                
                self.font.set_underline(True)
                self.font.set_bold(True)

                self.objectText = self.font.render(item[0], True, self.text_color)

            self.textRect = self.objectText.get_rect()
            self.textRect.center = self.listAppearance.get_rect().center

            self.textRect.centery += (placement * self.distanceBetweenWords) + self.listPlacement[1]
            self.textRect.centery -= self.listAppearance.get_rect().size[1] / 2
            self.textRect.centerx += self.listPlacement[0]

            t_screen.blit(self.objectText, self.textRect)

            placement = placement + 1

    def DidPlayerFindAllItems(self):

        for item in self.objectList: 
            if (not item[1]):
                return False
        
        return True
        

    objectList = []
    listAppearance = 0
    text_color = (0, 0, 0)
    cross_out_colour = (100,100,100)
    textRect = 0
    distanceBetweenWords = 30

    font = pygame.font.SysFont('franklingothicmedium', 18)
    objectText = font.render('', True, text_color)

    listPlacement = (1098,5)
