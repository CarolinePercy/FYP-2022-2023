import sys
from . import button

from . import FindableItem
from .. import globals
import pygame



class EditorItem(FindableItem.FindableItem):

    def __init__(self, img, location):

        self.image = img  

        self.ChangePosition(location[0], location[1])
        self.originalPosition = [location[0], location[1]]
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def Update(self):

        if (self.pressed):

            mouse = pygame.mouse.get_pos()
            self.ChangePosition(mouse[0] - (self.width / 2), mouse[1] - (self.height / 2))

        if (self.onScreen and self.pressed):
            None
            #print("Im out!")

    def Hover(self,t_event):

        if (t_event.type != pygame.MOUSEMOTION):
            self.pressed = False

    def UIMove(self, movement):
        if (not self.onScreen):

            self.position[0] += movement[0]
            self.position[1] += movement[1]
            self.imageRect = [self.position[0], self.position[1], self.width, self.height]
            
        self.originalPosition[0] += movement[0]
        self.originalPosition[1] += movement[1]

    def Press(self):
        mouse = pygame.mouse.get_pos()

        left = self.position[0]
        right = self.width + self.position[0]
        top = self.position[1]
        bottom = self.height + self.position[1]

        if (left <= mouse[0] <= right and top <= mouse[1] <= bottom and self.visible):
            self.ChangePosition(mouse[0] - (self.width / 2), mouse[1] - (self.height / 2))
            self.pressed = True
            return True

        self.pressed = False
        return False
        
    def processEvents(self, t_event, listRect):

        if (t_event.type == pygame.MOUSEBUTTONUP and 
        t_event.button == 1 and not self.onScreen and self.pressed):
            self.ChangePosition(self.originalPosition[0],self.originalPosition[1])
            #None
        
        super(FindableItem.FindableItem, self).processEvents(t_event)

        if (self.pressed):
            self.onScreen = not self.buttonRect.colliderect(listRect)

        
    originalPosition = [0,0]
    pressed = False
    onScreen = False
    visible = True