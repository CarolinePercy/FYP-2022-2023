import requests_cache
import pygame
import os
import asyncio

import json

from PIL import Image
import io

from .. import globals



class imageController():

    def RequestBackgrounds(self, input, amount = 2):
        imageRequest = self.RefineInput(input, globals.ImageType.BACKGROUND)
        return self.APIImageRequest(imageRequest, amount)

    def RequestItems(self, input, amount = 10):
        imageRequest = self.RefineInput(input, globals.ImageType.ITEM)
        return self.APIImageRequest(imageRequest, amount)

    def GetImages(self, response, amount):
        #self.currentRequestsAvailable = int(response.headers.get('X-RateLimit-Remaining'))
        finalList = []
        imList = self.DecodeResponse(response)
        currentExtraTag = (0,0)

        if len(imList) > 0:

            x = 0

            for image in imList:
                finalList.append(self.DecodeImage(image["webformatURL"]))
                x += 1

                if (x >= amount):
                    break
            
            while (x < amount):
                tag = self.GetTag(imList, currentExtraTag)
                nextList = self.DecodeResponse(self.session.get(self.RefineInput(tag, globals.ImageType.ITEM)))

                for image in nextList:
                    finalList.append(self.DecodeImage(image["webformatURL"]))
                    imList.append(image)
                    x += 1

                    if (x >= amount):
                        break
            
                currentExtraTag = (currentExtraTag[0], currentExtraTag[1] + 1)

                if (currentExtraTag[1] >= len(self.tags)):
                    currentExtraTag = [currentExtraTag[0] + 1, 0]
                    #return self.GetTag(decodedResponse, currentExtraTag)
                

            return finalList
                    
        else:
            print("No images match that theme.")

    def DecodeResponse(self, originalResponse):
        arrayString = originalResponse.content.decode('utf8')

        json_object = json.loads(arrayString)

        imList = json_object['hits']

        return imList

    def DecodeImage(self, imageURL):
        r = self.session.get(imageURL)

        img = io.BytesIO(r.content)

        img = pygame.image.load(img).convert_alpha()

        return img

    def GetTag(self, decodedResponse, tagIndex):
        self.tags = decodedResponse[tagIndex[0]]["tags"].split()
                
        y = 0
        for tag in self.tags:

            self.tags[y] = tag.replace(',', '')
            y += 1

        return self.tags[tagIndex[1]]

    def APIImageRequest(self, input, amount):

        nullSurface = [pygame.Surface((0,0))]

        if (self.CheckRequestLimit(input)):

            response = self.session.get(input)

            if response.ok:

                return self.GetImages(response, amount)

            else:
                print(response.reason)
                return nullSurface

        return nullSurface

    def getLocalImage(self,path):

         pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
         pygame.init()

         imp = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), path)).convert_alpha()
         return imp

    def Update(self, timePassed):

        if (len(self.requestTimers) > 0):

            self.requestTimers[0] -= timePassed

            if self.requestTimers[0] <= 0:

                #print("New request available")
                self.requestTimers.remove(self.requestTimers[0])

                if self.currentRequestsAvailable < self.maxRequestsPerMin:
                   

                    self.currentRequestsAvailable += 1
    
    def RefineInput(self, input, type):

        if " " in input:

            words = input.split()
            newInput = ""

            for w in words:
                newInput += "+" + w

            newInput = newInput[1:]
            input = newInput

        result = "https://pixabay.com/api/?q=" + input

        if (type == globals.ImageType.BACKGROUND):
            #result += "+interior"
            result += "&category=background"
            result += "&min_width=" + str(globals.SCREEN_WIDTH)
            result += "&min_height=" + str(globals.SCREEN_HEIGHT)

        elif (type == globals.ImageType.ITEM):
            result += "&colors=transparent"

        result += "&image_type=photo"
        result += "&key=" + self.key
        result += "&safesearch=true"

        return result

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

    tags = []
    numberOfTags = 0
    key = "30783872-c5a38bc80f3c7265ec4f5515c"

    session = requests_cache.CachedSession('userCache')