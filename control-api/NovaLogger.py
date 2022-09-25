import os
from Hologram.HologramCloud import HologramCloud

class NovaLogger:
  __device_key = os.getenv('NOVA_DEVICE_KEY')

  def __init__(self):
    self.hologram = HologramCloud({'devicekey': self.__device_key}, network='cellular')

  def send_to_influx(self, given_data_point):
    self.hologram.sendMessage(given_data_point.json())
