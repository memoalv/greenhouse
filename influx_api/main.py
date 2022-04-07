from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
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

@app.get("/ping")
def pong():
  return "pong"

@app.post("/log")
def log_data(data_point: DataPoint):
  data_logger.write(data_point)

  return "Data saved correctly"
