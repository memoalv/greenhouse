from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from DataPoint import DataPoint
from NovaLogger import NovaLogger

app = FastAPI()
nova_logger = NovaLogger()

@app.get("/ping")
def pong():
  return "pong"

@app.post("/log")
def log_data(data_point: DataPoint):
  nova_logger.send_to_influx(data_point)

  return "Data sent correctly"