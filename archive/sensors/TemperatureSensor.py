
class TemperatureSensor:

    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.rawReading = None
        self.temperature = None
        self.readTemp()

    def readTemp(self):
        with open(f'/sys/bus/w1/devices/{self.mac_address}/w1_slave', 'r') as f:
            self.rawReading = f.readlines()
        self.parseRawReading()

    def parseRawReading(self):
        tempLine = self.rawReading[1]
        temp = tempLine.split('t=')[1]
        self.temperature = int(temp) / 1000


if __name__ == "__main__":
    sensor = TemperatureSensor('28-030897946307')
    print(sensor.temperature)

        
