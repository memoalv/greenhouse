import datetime as dt
import csv
import uuid
import requests
from Emails import Emails

class Requests:

    def __init__(self):
        self.baseURL = 'https://api.deldesierto.org'
        self.authorization = {
            'Authorization': '59f02390-a2a3-4dc1-b19d-3c37d8933fa0'
        }

    def logTemps(self, temps):

        newItem = {
            'insideTemp': temps[0],
            'outsideTemp': temps[1],
            'cpuTemp': temps[2],
            'created': dt.datetime.now(),
            'uuid': str(uuid.uuid4())
        }

        res = requests.post(
            f'{self.baseURL}/climate/logData', headers=self.authorization, data=newItem)

        if res.status_code != 200:
            print(res, res.status_code, res.text)

            emails = Emails()
            emails.sendEmail(
                "Notificacion", f'Error del Api. Código de error: {res.status_code} -- Res {res.text}')
            with open('/home/pi/log/temp_log_backup.csv', 'a') as f:
                writer = csv.writer(f)
                data = []
                for temp in temps:
                    data.append(temp)

                data.append(dt.datetime.now())
                data.append(str(uuid.uuid4()))
                writer.writerow(data)
