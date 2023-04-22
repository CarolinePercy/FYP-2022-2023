import pygame

from .. import globals
from ..RestAPI import imageRetriever
from . import EditorItem, FindableItem
import copy

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

        if not isinstance(item, EditorItem.EditorItem) and isinstance(item, FindableItem.FindableItem):

            try:
                silhouette = item.image.copy()

                w, h = silhouette.get_size()
                for x in range(w):
                    for y in range(h):
                            a = silhouette.get_at((x, y))[3]
                            silhouette.set_at((x, y), pygame.Color(0, 0, 0, a))

                if (silhouette.get_height() > 100):
                    newSize = ((100 / silhouette.get_height()) * silhouette.get_width(), 100)
                    silhouette = pygame.transform.scale(silhouette, newSize)
                self.objectList.append([silhouette, False])

            except Exception as e:
                print(e)


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

    def ResetList(self):
        for item in self.objectList:

            item[1] = False

            if isinstance(item[0], FindableItem.FindableItem):
                item[0].Toggle(True)

    def EmptyList(self):
        self.objectList.clear()   

    def Draw(self, t_screen):

        t_screen.blit(self.listAppearance, self.listPlacement)
        listMask = pygame.mask.from_surface(self.listAppearance)

        if len(self.objectList) > 0:

            placement = 1

            for item in self.objectList:

                if (type(item[0]) is pygame.Surface):
                    if (not item[1]):
                        
                        self.textRect = item[0].get_rect()
                        self.textRect.center = self.listAppearance.get_rect().center

                        self.textRect.centery += self.listPlacement[1] 
                        self.textRect.centery -= max((self.listAppearance.get_rect().size[1] /2) - self.textRect.size[1], 0) 

                        self.textRect.centery += self.distanceBetweenWords

                        self.textRect.centerx += self.listPlacement[0]

                        offsetY = self.textRect.y - self.listPlacement[1]

                        overlapMask = listMask.overlap_mask(pygame.mask.from_surface(item[0]), (0, offsetY))
                        overlapSurface = overlapMask.to_surface(setcolor=(1, 1, 1))
                        overlapSurface.set_colorkey((0, 0, 0))

                        self.distanceBetweenWords +=  self.textRect.height + self.distStart

                        self.textRect.y = 0
                        t_screen.blit(overlapSurface, self.textRect)
                        #placement = placement + 1

                elif (isinstance(item[0], EditorItem.EditorItem) and not item[0].onScreen):
                    item[0].Draw(t_screen)

                elif (isinstance(item[0], FindableItem.FindableItem)):
                    item[0].Draw(t_screen)

        self.textRect = pygame.Rect(0,0,0,0)
        self.distanceBetweenWords = 0
        
    def DidPlayerFindAllItems(self):

        if len(self.objectList) > 0:
            for item in self.objectList: 
                if (not item[1] and isinstance(item[0], FindableItem.FindableItem)):
                    return False
            
            return True

        else:
            return False
        
    def UpdateRect(self):
        self.listRect.update(self.listPlacement[0],self.listPlacement[1], 
        self.listSize[0], self.listSize[1])
    
    def Update(self):

        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem):
                item[0].Update()
            
    def ProcessEvents(self, t_event):

        prevFound = False

        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem):
                item[0].processEvents(t_event, self.listRect)

            elif isinstance(item[0], FindableItem.FindableItem):
                check = item[0].processEvents(t_event)

                if (check):
                    item[1] = True
                    prevFound = True
                
                    item[0].Toggle(False)
            elif isinstance(item[0], pygame.Surface):
                if (prevFound):
                    item[1] = True
                    prevFound = False

    def GetOnScreenItems(self):
        newList = []

        for item in self.objectList:
            if isinstance(item[0], EditorItem.EditorItem) and item[0].onScreen:
                newList.append(item[0])

        return newList

    objectList = 0
    textRect = pygame.Rect(0,0,0,0)
    distStart = 30
    distanceBetweenWords = 0


    listAppearance = 0
    listSize = []
    listRect = None
    
    listPlacement = 0
