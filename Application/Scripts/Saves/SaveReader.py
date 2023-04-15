import json
import pygame
from ..RestAPI import imageRetriever
from ..UI import list, FindableItem
from .. import background


class SaveStorer():

    def ReadDataFromJSON(self,nameOfLevel):

        fileName = "../Saves/JSON_Saves/" + nameOfLevel + '.json'

        try:

            with open(fileName, 'r') as openfile:
        
                json_object = json.load(openfile)
        
            self.ConvertJSONToData(json_object)

        except Exception as e:

            #if (type(e) == FileNotFoundError):
            #    print("No file found with that name.")

            #else:
                print(e)

    def ConvertJSONToData(self, data):

        self.GetItems(data)
        self.GetBackground(data)

    def GetItems(self, data):
        
        for item in data['items']:
            location = (float(item['position']['x']), float(item['position']['y']))
            #image = imageRetriever.imageController().getLocalImage(item['image'])

            #newItem = EditorItem.EditorItem(image, location)

            newItem = FindableItem.FindableItem(item['image'])
            newItem.ChangePosition(location[0], location[1])
            self.itemList.AddToList(newItem)


    def GetBackground(self, data):
        #self.background = imageRetriever.imageController().getLocalImage(data['background'])
        self.background = background.image(data['background'])

    background = ""
    itemList = list.List()
