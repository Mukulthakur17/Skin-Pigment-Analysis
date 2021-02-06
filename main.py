from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import shutil
from pathlib import Path
import json

app = FastAPI()


@app.get('/')
async def home():
    return {"Hello":"There"}

@app.post('/predict')
async def predict(image: UploadFile = File(...)):
    temp_file = save_to_disk(image, path="temp", save_as='temp')
# add model and return diagnosis report
    return "Diagnosis"
   


def save_to_disk(uploadedfile, path='.', save_as='default'):
    extension = os.path.splitext(uploadedfile.filename)[-1]
    temp_file = os.path.join(path, save_as+extension)
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(uploadedfile.file, buffer)
    return temp_file

if __name__ =='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8080)