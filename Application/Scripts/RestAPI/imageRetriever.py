import requests_cache
import pygame
import os
import asyncio

import json

from PIL import Image
import io

from .. import globals



class imageController():

    def APIImageRequest(self, input, type = globals.ImageType.DEFAULT, specific = False):

        if (self.CheckRequestLimit(input)):

            nullSurface = pygame.Surface((0,0))

            apiText = ""

            if not specific:
                apiText = self.RefineInput(input)

            else:
                apiText = input

            response = self.session.get(apiText)

            if response.ok:

                #print(response.headers.get('X-RateLimit-Limit'))
                print(response.headers.get('X-RateLimit-Remaining'))
                #print(response.headers.get('X-RateLimit-Reset'))     

                self.currentRequestsAvailable = int(response.headers.get('X-RateLimit-Remaining'))

                arrayString = response.content.decode('utf8')

                json_object = json.loads(arrayString)

                imList = json_object['hits']

                if len(imList) > 0:
                    url = imList[0]["webformatURL"]

                    if (self.CheckRequestLimit(input)):
                    
                        r = self.session.get(url)

                        img = io.BytesIO(r.content)

                        img = pygame.image.load(img)

                        return img
                    
                else:
                    return nullSurface
                    print("No images match that theme.")

            else:
                print(response.reason)
                return nullSurface

    def getLocalImage(self,path):

         pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
         pygame.init()

         imp = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), path))
         return imp

    def Update(self, timePassed):

        if (len(self.requestTimers) > 0):

            self.requestTimers[0] -= timePassed

            if self.requestTimers[0] <= 0:

                print("New request available")
                self.requestTimers.remove(self.requestTimers[0])

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

    async def CheckRequestLimitCoroutine(self, request):

        if self.currentRequestsAvailable > 0:
            await asyncio.sleep(0)
            return True
   
        else:
            self.requestStash.append(request)

            while (self.currentRequestsAvailable <= 0):
                await asyncio.sleep(1)

            return True

    def CheckRequestLimit(self, request):
        coro =  self.CheckRequestLimitCoroutine(request)
        result = asyncio.run(coro)

        self.requestTimers.append(self.requestRefreshRate)

        return result

    maxRequestsPerMin = 100
    currentRequestsAvailable = 100
    requestRefreshRate = 0.6
    requestTimers = []

    requestStash = []

    inst = None

    session = requests_cache.CachedSession('userCache')