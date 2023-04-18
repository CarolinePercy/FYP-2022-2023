import json
import pygame
import os
from pathlib import Path

def SaveDataToJSON(nameOfLevel, saveData):

    try:
        json_object = json.dumps(saveData, indent=4)

        fileName = "../Saves/JSON_Saves/" + nameOfLevel + ".json"

        with open(fileName, "w") as outfile:
            outfile.write(json_object)


    except Exception as e:
        print(e)
        print(type(saveData))

def ConvertDataToJSON(nameOfLevel, items, background):

    itemSaveData = SaveImages(items, nameOfLevel)
    backgroundSaveData = SaveBackground(background, nameOfLevel)
    
    saveData = {

        "items": itemSaveData,
        "background": backgroundSaveData

    }

    nameOfLevel = nameOfLevel.replace(" ", "_")

    if (type(saveData) is not dict):

        print(type(saveData))

    else:
        SaveDataToJSON(nameOfLevel, saveData)  

def SaveImages(items, nameOfLevel):

    imageNum = 1
    name = ""
    path = os.path.join(Path(os.getcwd()).parents[1], 'Assets\\AutoSavedAssets\\', name)
    storedSave = ""

    saveData = []

    for i in items:

        name = nameOfLevel + str(imageNum) + ".png"

        storedSave = CheckDirectory(nameOfLevel, i.image, name)

        saveData.append({"position" : { "x": str(i.position[0]), "y": str(i.position[1])}, "image" : str(storedSave)})
        imageNum += 1

    return saveData

def SaveBackground(background, nameOfLevel):

    name = nameOfLevel + "BG.png"

    saveData = CheckDirectory(nameOfLevel, background, name)
    
    return saveData

def CheckDirectory(nameOfLevel, image, name):

    path = os.path.join(Path(os.getcwd()).parents[1], 'Assets\\AutoSavedAssets\\', nameOfLevel, name)
    saveData = "../Assets/AutoSavedAssets/" + nameOfLevel + "/" + name

    try:
        pygame.image.save(image, path)
            
    except:
        os.mkdir(Path(path).parents[0])
        pygame.image.save(image, path)  

    return saveData
