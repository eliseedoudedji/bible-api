from typing import Optional

from fastapi import FastAPI
import json

app = FastAPI()

with open('bible.json', "r") as f:
        data = json.load(f)
   

@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/chapitre/{id}")
def read_item(id):
    id= int(id)
    chapter =[]
    long= len(data['Testaments'][0]['Books'][0]["Chapters"][id]['Verses'])
    for i in range(0,long):
        chapter.append(data['Testaments'][0]['Books'][0]["Chapters"][id]['Verses'][i]['Text'])

    return chapter

@app.get("/livres/{id}")
def read_item(id):
    id= int(id)
    chapter =[]
    long= len(data['Testaments'][id]['Books'])
    for i in range(0,long):
        chapter.append(data['Testaments'][id]['Books'][i]['Text'])

    return chapter

@app.get("/testament/{id}")
def read_item(id):
    id= int(id)

    chapter =[]
    # long= len(data['Testaments'][id])
    # for i in range(0,long):
    #     chapter.append(data['Testaments'][0]['Books'][i]['Text'])

    return data['Testaments'][id]['Text']