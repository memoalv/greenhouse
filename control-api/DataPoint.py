from typing import Optional
from pydantic import BaseModel

class DataPoint(BaseModel):
  node: str
  temperature: Optional[float] = None
  air_humidity: Optional[float] = None
  lux: Optional[float] = None
  soil_humidity: Optional[float] = None