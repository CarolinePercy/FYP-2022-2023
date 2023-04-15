import pygame
from ..Saves import SaveReader, SaveWriter

from .. import globals

from ..RestAPI import imageRetriever

from . import button, list, EditorItem

import time

class EditorScreen():



    def __init__(self):


        self.listOfObjects.ChangeSize((self.listWidth,740))        


        self.menuButton.ChangePosition(globals.SCREEN_WIDTH - self.menuButton.buttonRect[2], 20)


        self.listOfObjects.ChangePosition((globals.SCREEN_WIDTH, -10))  
         

        self.saveButton.ChangePosition(self.saveButton.width + 5, 5) 

        self.saveButton.ChangeText('Save Level')

        self.image[0].set_alpha(0)


    def Draw(self, t_screen):


        t_screen.blit(pygame.transform.scale(self.image[0], 

        (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)), (0, 0))


        self.menuButton.Draw(t_screen)


        self.saveButton.Draw(t_screen)


        self.listOfObjects.Draw(t_screen)


    def Update(self, dt):
        self.listOfObjects.Update()


    def RetrieveItemsAndBackground(self, input):

        self.image = self.imageGet.RequestBackgrounds(input)
        images = self.imageGet.RequestItems(input)


        imageYStart = 50


        for oneImage in images:


            oneImage = self.ResizeItemImage(oneImage)


            self.listOfObjects.AddToList(EditorItem.EditorItem(oneImage, (globals.SCREEN_WIDTH + (self.listWidth / 2) - (self.itemStartingWidth / 2)

            ,imageYStart)))


            imageYStart += oneImage.get_height() + self.itemDistanceOnList


    def ProcessEvents(self, t_event):


        menuCheck = self.menuButton.processEvents(t_event)

        saveCheck = self.saveButton.processEvents(t_event)


        if (menuCheck):


            if (self.editorOpen):


                self.menuButton.ChangePosition(globals.SCREEN_WIDTH - self.menuButton.width, 20)


                self.listOfObjects.ChangePosition((globals.SCREEN_WIDTH, self.listOfObjects.listPlacement[1])) 


                self.listOfObjects.MoveItems((self.listOfObjects.listSize[0],0))               
             


            else:


                self.listOfObjects.ChangePosition((globals.SCREEN_WIDTH - self.listOfObjects.listSize[0], self.listOfObjects.listPlacement[1]))


                self.menuButton.ChangePosition(self.listOfObjects.listPlacement[0] - self.menuButton.width, 20)


                self.listOfObjects.MoveItems((-self.listOfObjects.listSize[0], 0))



            self.editorOpen = not self.editorOpen


        if (saveCheck):
            self.SaveLevel()


        if (t_event.type == pygame.MOUSEWHEEL):

            self.listOfObjects.MoveItems((0, t_event.y * self.listScrollSpeed))


        self.listOfObjects.ProcessEvents(t_event)


    def ResizeItemImage(self, image):

        aimedWidth = max(image.get_width(), self.itemStartingWidth)


        sizeDifference = 0


        if (aimedWidth > self.itemStartingWidth):

            sizeDifference = image.get_width() / self.itemStartingWidth

            return pygame.transform.scale(image, (image.get_width() / sizeDifference, image.get_height() / sizeDifference))


        elif (aimedWidth < self.itemStartingWidth):

            sizeDifference = self.itemStartingWidth / image.get_width()

            return pygame.transform.scale(image, (image.get_width() / sizeDifference, image.get_height() / sizeDifference))

        return image


    def ResetEditor(self):

        self.listOfObjects.EmptyList()
        self.image[0].set_alpha(0)


        if (self.editorOpen):

                self.menuButton.ChangePosition(globals.SCREEN_WIDTH - self.menuButton.width, 20)


                self.listOfObjects.ChangePosition((globals.SCREEN_WIDTH, self.listOfObjects.listPlacement[1])) 


                self.listOfObjects.MoveItems((self.listOfObjects.listSize[0],0))    


                self.editorOpen = False


    def SaveLevel(self):
        SaveWriter.ConvertDataToJSON("test", self.listOfObjects.GetOnScreenItems(), self.image[0])


    editorOpen = False



    font = pygame.font.SysFont('franklingothicmedium', 18)



    text_color = (0, 0, 0)


    textObject = ""



    textRect = font.render('', True, text_color)



    menuButton = button.Button((33,49),"MenuButton.png")

    leftButton = button.Button((33,49),"ArrowButton.png")
    rightButton = button.Button((33,49),"ArrowButton.png")
    saveButton = button.Button()


    listOfObjects = list.List(True)


    imageGet = imageRetriever.imageController()


    listWidth = 300

    itemStartingWidth = listWidth / 2

    itemDistanceOnList = 10

    listScrollSpeed = 30

    image = [pygame.Surface((0,0))]
     