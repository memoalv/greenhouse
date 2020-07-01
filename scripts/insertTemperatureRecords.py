from pymongo import MongoClient
import csv
import uuid
import requests

client = MongoClient('localhost', 27017)

db = client.greenhouse

temps = []

with open('/home/memo/temp_log.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    inserted_rows = 0
    for row in csv_reader:

        newItem = {}

        if row["temp"]:
            newItem["insideTemp"] = float(row["temp"])

        if row["outsideTemp"]:
            newItem["outsideTemp"] = float(row["outsideTemp"])

        if row["cpuTemp"]:
            newItem["cpuTemp"] = float(row["cpuTemp"])

        if row["date"]:
            newItem["created"] = row["date"]

        if row["uuid"]:
            newItem["uuid"] = row["uuid"]
        else:
            newItem["uuid"] = str(uuid.uuid4())

        print(newItem)

        line_count += 1
        # res = db.tempLog.insert_one(row)

        headers = {
            'Authorization': '59f02390-a2a3-4dc1-b19d-3c37d8933fa0'
        }

        res = requests.post(
            'https://api.deldesierto.org/climate/logData', headers=headers, data=newItem)

        if res.status_code == 200:
            inserted_rows += 1
        else:
            print(res)
        # if res.inserted_id:
            # inserted_rows += 1

    print(f'Total documents: {line_count}')
    print(f'Inserted documents: {inserted_rows}')
