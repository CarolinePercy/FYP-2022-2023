import json
import pygame
from ..RestAPI import imageRetriever
from ..UI import list, FindableItem
from .. import background


class SaveStorer():

    def ReadDataFromJSON(self,nameOfLevel):

        nameOfLevel = nameOfLevel.replace(" ", "_")

        fileName = "../Saves/JSON_Saves/" + nameOfLevel + '.json'

        try:

            with open(fileName, 'r') as openfile:
        
                json_object = json.load(openfile)
        
            self.ConvertJSONToData(json_object)
            return False

        except Exception as e:
            print(e)
            return True

    def ConvertJSONToData(self, data):

        self.GetItems(data)
        self.GetBackground(data)

    def GetItems(self, data):

        self.itemList.EmptyList()
        
        for item in data['items']:
            location = (float(item['position']['x']), float(item['position']['y']))

            newItem = FindableItem.FindableItem(item['image'])
            newItem.ChangePosition(location[0], location[1])
            self.itemList.AddToList(newItem)


    def GetBackground(self, data):
        self.background = background.image(data['background'])

    background = ""
    itemList = list.List()
