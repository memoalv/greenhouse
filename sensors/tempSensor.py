#!/usr/bin/python3

import os
import datetime as dt
import csv
from Relay import Relay
from Display import Display
import time
import uuid

# load modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# read raw sensor output
def readRawData(sensor, outsideSensor):
    sensorsRawTemp = None
    outsideSensorsTemp = None
    cpuTemp = None

    # open sensors dump file to read lines
    with open(f'/sys/bus/w1/devices/{sensor}/w1_slave', 'r') as f:
        sensorsRawTemp = f.readlines()

    # open sensors dump file to read lines
    with open(f'/sys/bus/w1/devices/{outsideSensor}/w1_slave', 'r') as f:
        outsideSensorsTemp = f.readlines()

    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f2:
        cpuTemp = list(f2)

    return sensorsRawTemp, outsideSensorsTemp, cpuTemp

# parse raw data to get the temperature
def parseRawData(data):
    tempLine = data[1]
    temp = tempLine.split('t=')[1]
    return int(temp)


def logTemps(temps):
    with open('/home/pi/log/temp_log.csv', 'a') as f:
        writer = csv.writer(f)
        data = []
        for temp in temps:
            data.append(temp)
        data.append(dt.datetime.now())
        data.append(str(uuid.uuid4()))

        writer.writerow(data)


def main():
    # sensors mac addresses
    sensor = '28-030897946307'
    outsideSensor = '28-031297940783'

    rawFrontSensorData, rawOutsideSensor, cpuRawData = readRawData(
        sensor, outsideSensor)

    insideSensorTemp = parseRawData(rawFrontSensorData) / 1000
    outsideSensorTemp = parseRawData(rawOutsideSensor) / 1000
    insideSensorTemp = '%.2f' % (insideSensorTemp)
    outsideSensorTemp = '%.2f' % (outsideSensorTemp)

    cpuTemp = int(cpuRawData[0].rstrip()) / 1000
    cpuTemp = '%.2f' % (cpuTemp)

    logTemps([insideSensorTemp, outsideSensorTemp, cpuTemp])
    
    display = Display()
    display.printMessage(
        f'Adentro: {insideSensorTemp} C\nAfuera: {outsideSensorTemp} C\nTemp CPU: {cpuTemp}')

    print(f'CPU TEMP: {cpuTemp}° C')
    print(f'FRONT SENSORS TEMP: {insideSensorTemp}° C')
    print(f'OUTSIDE SENSORS TEMP: {outsideSensorTemp}° C')


startup = True
while True:
    if startup:
        main()
    startup = False
    time.sleep(300)
    main()
