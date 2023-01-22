import requests
import json
import io

class APIWrapper():

    def getImagesFromTheme(self, theme):
        apiText = "https://pixabay.com/api/?key=30783872-c5a38bc80f3c7265ec4f5515c&q=christmas&image_type=photo"

        response = requests.get(apiText)

        arrayString = response.content.decode('utf8').replace("'", '"')
        json_object = json.loads(arrayString)

        imList = json_object['hits']

        #url = imList[0]["webformatURL"]

        for url in imList["webformatURL"]:
            print(url)

        #r = requests.get(url)
        #img = io.BytesIO(r.content)
        #return img