import requests_cache
import pygame
import os

import json

from PIL import Image
import io

from .. import globals


class imageController():

    def APIImageRequest(self, input, specific = False):

        if self.currentRequestsAvailable > 0:

            apiText = ""

            if not specific:
                apiText = self.RefineInput(input)

            else:
                apiText = input

            response = self.session.get(apiText)
            #self.session.urls.len()

            arrayString = response.content.decode('utf8').replace("'", '"')

            json_object = json.loads(arrayString)


            imList = json_object['hits']


            url = imList[0]["webformatURL"]

            r = self.session.get(url)

            img = io.BytesIO(r.content)

            img = pygame.image.load(img)

            return img
        
        else:
            t = 0

    def getLocalImage(self,path):

         pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
         pygame.init()

         imp = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), path))
         return imp

    def Update(self, timePassed):

        for t in self.requestTimers:
            t -= timePassed

            if t <= 0:

                self.requestTimers.remove(t)

                if self.currentRequestsAvailable < self.maxRequestsPerMin:
                    self.currentRequestsAvailable += 1

    def RefineInput(self, input):

        if " " in input:

            words = input.split()
            newInput = ""

            for w in words:
                newInput += "+" + w

            newInput = newInput[1:]
            input = newInput

        return "https://pixabay.com/api/?q=" + input + "&key=30783872-c5a38bc80f3c7265ec4f5515c"


    maxRequestsPerMin = 100
    currentRequestsAvailable = 100
    requestTimers = []

    session = requests_cache.CachedSession('userCache')