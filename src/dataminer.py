import csv
from CONFIG import pin
from datetime import datetime
#import Adafruit_DHT
from core import Database


#sensor = Adafruit_DHT.DHT22
db = Database()

class Dataminer:

    def get_h_t(self) -> dict:
        #hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        hum, temp  = 22.13123, 50.38293
        data = {"humidity": round(hum, 2), "temperature": round(temp, 2), "timestamp": self.utcnow()}
        self.push_to_db(data)
        self.push_to_csv(data)
        return data

    @staticmethod
    def push_to_db(data: dict):
        return

    @staticmethod
    def push_to_csv(data:dict):
        fieldnames = ["humidity", "temperature", "timestamp"]
        dir = "./src/csv/data.csv"

        with open(dir, "w") as file:
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerow(data)

    @staticmethod
    def utcnow():
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def read_csv() -> list:
        csv_values = []
        with open("src/csv/data.csv", "r") as cf:
            csvreader = csv.DictReader(cf)
            for raw in csvreader:
                data = {"humidity": raw["humidity"], "temperature": raw["temperature"], "timestamp": raw["timestamp"]}
                csv_values.append(data)
        
        return csv_values