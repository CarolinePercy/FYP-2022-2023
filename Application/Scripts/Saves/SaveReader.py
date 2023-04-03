import json

def ReadDataFromJSON(nameOfLevel):

    fileName = "../Saves/JSON_Saves/" + nameOfLevel + '.json'

    try:

        with open(fileName, 'r') as openfile:
    
            json_object = json.load(openfile)
    
        ConvertJSONToData(json_object)

    except Exception as e:

        if (type(e) == FileNotFoundError):
            print("No file found with that name.")

        else:
            print(e)

def ConvertJSONToData(data):
    print(data)
    print(type(data))