import requests
import pygame
import os
import json
from PIL import Image
import io
import globals

class imageController():

    def getAPIImage():
        apiText = "https://pixabay.com/api/?q=white+bloom&id=729510&editors_choice=true&pretty=true&key=30783872-c5a38bc80f3c7265ec4f5515c"

        response = requests.get(apiText)

        arrayString = response.content.decode('utf8').replace("'", '"')
        json_object = json.loads(arrayString)

        imList = json_object['hits']

        url = imList[0]["webformatURL"]

        r = requests.get(url)
        img = io.BytesIO(r.content)
        return img

    def getLocalImage(self,path):
         pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
         pygame.init()
         imp = pygame.image.load(os.path.join(os.path.dirname(__file__), path))
         return imp

    