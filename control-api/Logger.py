import os
from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

class Logger:
  __token = os.getenv('INFLUX_TOKEN')
  __org = os.getenv('INFLUX_ORG')
  __bucket = os.getenv('INFLUX_BUCKET')

  def __init__(self):
    client = InfluxDBClient(
      url=os.getenv('INFLUX_URL'),
      token=self.__token,
      org=self.__org
    )
    self.write_api = client.write_api(write_options=SYNCHRONOUS)

  def write(self, given_data_point):
    data_points = self.__create_influx_data_points(given_data_point)

    for data_point in data_points:
      self.write_api.write(self.__bucket, self.__org, data_point)

  def __create_influx_data_points(self, given_data_point):
    data_points = []
    for measurement, reading in given_data_point.dict().items():
      if measurement == "node":
        pass

      data_points.append(
        {
          "measurement": measurement,
          "tags": {"node": given_data_point.node},
          "fields": {"reading": reading},
          "time": datetime.utcnow()
        }
      )

    return data_points
