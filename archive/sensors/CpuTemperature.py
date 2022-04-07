
class CpuTemperature:

    def __init__(self):
        self.rawReading = None
        self.temperature = None
        self.readTemp()

    def readTemp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f2:
            self.rawReading = list(f2)
            self.parseRawReading()

    def parseRawReading(self):
        tmp = int(self.rawReading[0].rstrip()) / 1000
        self.temperature = '%.2f' % (tmp)


if __name__ == "__main__":
    sensor = CpuTemperature()
    print(sensor.temperature)

        
