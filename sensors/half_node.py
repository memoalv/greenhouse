import network
from machine import Pin, I2C
from time import sleep
import dht
from veml7700 import VEML7700
import urequests as req
import ujson

wifi_network = "greenhouse-main"
wifi_password = "greenhouse_wsn"
control_api = "http://10.10.10.1:8000"

station = network.WLAN(network.STA_IF)
if not station.isconnected():
    print("connecting to network...")
    station.active(True)
    station.connect(wifi_network, wifi_password)
    while not station.isconnected():
        print(station.status())
        sleep(2)
print("network config:", station.ifconfig())

# initialize temperature and humidity sensor
dht_sensor = dht.DHT22(Pin(4))

# initialize light sensor
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=10000)
lux_sensor = VEML7700(adress=0x10, i2c=i2c, it=100, gain=1 / 8)

while True:
    temp = None
    hum = None
    lux = None

    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
    except OSError as _:
        print("Failed to read DHT22.")
    try:
        lux = lux_sensor.read_lux()
    except OSError as _:
        print("Failed to read VEML.")
    print(temp, hum, lux)

    request_data = ujson.dumps({
        "node": "node 1",
        "temperature": temp,
        "air_humidity": hum,
        "lux": lux
        })
    res = req.post(url=f"{control_api}/log", data=request_data)
    print(res.text)
    
    sleep(300) # 5 min