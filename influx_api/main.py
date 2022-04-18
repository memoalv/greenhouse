from fastapi import FastAPI, Request, Response
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()
from Logger import Logger

class DataPoint(BaseModel):
  node: str
  temperature: Optional[float] = None
  air_humidity: Optional[float] = None
  lux: Optional[float] = None
  soil_humidity: Optional[float] = None

app = FastAPI()
data_logger = Logger()

@app.middleware("http")
async def authorize_request(request: Request, call_next):
    auth_token = request.headers['Authorization']
    if auth_token != os.getenv('API_KEY'):
      return Response(status_code=401)

    return await call_next(request)
    

@app.get("/ping")
def pong():
  return "pong"

@app.post("/log")
def log_data(data_point: DataPoint):
  data_logger.write(data_point)

  return "Data saved correctly"
