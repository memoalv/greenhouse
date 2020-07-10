#!/usr/bin/python3

import time
from Relay import Relay
from Display import Display
from CpuTemperature import CpuTemperature
from TemperatureSensor import TemperatureSensor
from Requests import Requests


def main():
    # lectura de sensores de temperatura
    insideSensor  = TemperatureSensor('28-030897946307') # sensor dentro del invernadero
    outsideSensor = TemperatureSensor('28-031297940783') # sensor fuera
    cpuSensor     = CpuTemperature()

    # se empujan los datos al API
    req = Requests()
    req.logTemps([
        insideSensor.temperature,
        outsideSensor.temperature,
        cpuSensor.temperature
    ])

    # control de abanicos
    # relay = Relay(24) # se controla con el pin 24
    # if insideSensor.temperature > 28:
    #     relay.turnOn()
    # else:
    #     relay.turnOn()

    # se muestran las lecturas en la pantalla
    display = Display()
    display.printMessage(
        f'Adentro: {insideSensor.temperature} C\nAfuera: {outsideSensor.temperature} C\nTemp CPU: {cpuSensor.temperature}')

    # se imprimen las lecturas para el syslog
    print(f'CPU TEMP: {cpuSensor.temperature}° C')
    print(f'INSIDE SENSORS TEMP: {insideSensor.temperature}° C')
    print(f'OUTSIDE SENSORS TEMP: {outsideSensor.temperature}° C')


if __name__ == "__main__":
    startup = True
    while True:
        if startup:
            main()
        startup = False
        time.sleep(300) # 5 min
        main()
