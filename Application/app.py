# import the pygame module
import pygame
import requests
from PIL import Image
#from io import BytesIO
import json
import numpy as np
import io


# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1200, 800))
  
# Set the caption of the screen
pygame.display.set_caption('Hidden Object REST API Game!')
  
# Fill the background colour to the screen
screen.fill(background_colour)

apiText = "https://pixabay.com/api/?q=white+bloom&id=729510&editors_choice=true&pretty=true&key=30783872-c5a38bc80f3c7265ec4f5515c"

response = requests.get(apiText)

arrayString = response.content.decode('utf8').replace("'", '"')
json_object = json.loads(arrayString)

imList = json_object['hits']

#im.show()

url = imList[0]["webformatURL"]

r = requests.get(url)
img = io.BytesIO(r.content)


#print(url)
#image_file.show()
image = pygame.image.load(img)
screen.blit(image, (100, 100))

  
# Update the display using flip
pygame.display.flip()
  
# Variable to keep our game loop running
running = True
  
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False