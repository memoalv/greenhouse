import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from Emails import Emails

emails = Emails()


class TempHumSensor:

    def __init__(self):
        self.tempSensorPin = 17
        self.tempSensor = Adafruit_DHT.DHT22

    def read(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(
            self.tempSensor, self.tempSensorPin)
        return (humidity, temperature)

    def reliableReading(self):
        errorsInReadings = []
        tempReadings = []
        for i in range(0, 5):
            try:
                humidity, temperature = Adafruit_DHT.read_retry(
                    self.tempSensor, self.tempSensorPin)
                tempReadings.append((temperature, humidity))
            except:
                errorsInReadings.append(True)

        if len(errorsInReadings) > 4:
            emails.sendEmail(
                "Notificacion", "Error al obtener las lecturas del sensor DHT22")

        avgTemp = 0
        avgHum = 0
        for reading in tempReadings:
            avgTemp += reading[0]
            avgHum += reading[1]

        avgTemp = avgTemp / len(tempReadings)
        avgHum = avgHum / len(tempReadings)
        return (avgTemp, avgHum)

