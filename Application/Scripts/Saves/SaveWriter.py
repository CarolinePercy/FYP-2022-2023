import json

def SaveDataToJSON(nameOfLevel, saveData):

    try:
        json_object = json.dumps(saveData, indent=4)

        fileName = "../Saves/JSON_Saves/" + nameOfLevel + ".json"

        with open(fileName, "w") as outfile:
            outfile.write(json_object)


    except Exception as e:
        print(e)

def ConvertDataToJSON(nameOfLevel, items, background):

    itemSaveData = []
    backgroundSaveData = {}
    
    for item in items:
        itemSaveData.append({"position" : "1", "image": "thj"})


    saveData = {

        "items": itemSaveData,
        "background": backgroundSaveData

    }

    SaveDataToJSON(nameOfLevel, saveData)

def SaveImages():
    None