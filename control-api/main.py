from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests as r
import json

import os
from dotenv import load_dotenv
load_dotenv()

class DataPoint(BaseModel):
  node: str
  temperature: float
  air_humidity: float
  lux: float
  soil_humidity: Optional[float] = None

app = FastAPI()

@app.get("/")
def index():
  return "OK"

@app.post("/log")
def log_data(data_point: DataPoint):
  response = r.post(
    f"{os.getenv('MONITORING_API_URL')}/climate",
    headers={'Authorization': os.getenv('AUTH_KEY') },
    json=json.loads(data_point.json())
  )

  if response:
    print('post success')
  else: 
    print('An error has occurred.')

  return "Success"
