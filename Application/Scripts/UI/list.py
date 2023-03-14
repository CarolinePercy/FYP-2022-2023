import pygame

from .. import globals
from ..RestAPI import imageRetriever
from . import EditorItem

class List():

    def __init__(self, longList = False):
        self.objectList = []

        if (longList):
            self.listAppearance = imageRetriever.imageController().getLocalImage("../Assets/ListAppearance1.png")

        else:
            self.listAppearance = imageRetriever.imageController().getLocalImage("../Assets/ListAppearance2.png")

        self.listPlacement = (1098,5)
        self.listRect = self.listAppearance.get_rect()

    def AddToList(self, item):
        self.objectList.append([item, False])

    def ChangeSize(self, size):
       self.listAppearance = pygame.transform.scale(self.listAppearance, size)
       self.listPlacement = (globals.SCREEN_WIDTH - size[0], 0)
       self.listSize = size
       self.UpdateRect()

    def ChangePosition(self, newPosition):
        self.listPlacement = newPosition
        self.UpdateRect()

    def MoveItems(self, movement):

        if (movement[1] != 0):
            if (movement[1] > 0 and self.objectList[0][0].position[1] >= 20
            or movement[1] < 0 and self.objectList[len(self.objectList)-1][0].position[1] <= 620):
                return


        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem):
                item[0].UIMove(movement)

    def FoundItem(self, item):

        index = 0
        for type in globals.Item:

            if (item == type):        
                self.objectList[index][1] = True
                
            index += 1

    def ResetList(self):
        for item in self.objectList:

            item[1] = False

    def EmptyList(self):
        self.objectList.clear()   

    def Draw(self, t_screen):

        if (len(self.objectList) > 0 and isinstance(self.objectList[0][0], EditorItem.EditorItem)):
            for item in self.objectList:
                if (item[0].onScreen):
                    item[0].Draw(t_screen)

        t_screen.blit(self.listAppearance, self.listPlacement)
        #surface = pygame.display.set_mode((globals.SCREEN_WIDTH,globals.SCREEN_HEIGHT))
        #pygame.draw.rect(surface, (255,1,1), self.listRect)
        placement = 1

        for item in self.objectList:

            if (type(item[0]) is str):
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

            elif (isinstance(item[0], EditorItem.EditorItem) and not item[0].onScreen):
                item[0].Draw(t_screen)

    def DidPlayerFindAllItems(self):

        for item in self.objectList: 
            if (not item[1]):
                return False
        
        return True
        
    def UpdateRect(self):
        self.listRect.update(self.listPlacement[0],self.listPlacement[1], 
        self.listSize[0], self.listSize[1])

    def Update(self):

        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem):
                item[0].Update()
            

    def ProcessEvents(self, t_event):

        loop = 0
        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem):
                item[0].processEvents(t_event, self.listRect)

            loop += 1

    objectList = 0
    text_color = (0, 0, 0)
    cross_out_colour = (100,100,100)
    textRect = 0
    distanceBetweenWords = 30

    listAppearance = 0
    listSize = []
    listRect = None

    font = pygame.font.SysFont('franklingothicmedium', 18)
    objectText = font.render('', True, text_color)

    listPlacement = 0
