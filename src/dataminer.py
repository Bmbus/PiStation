import csv
from CONFIG import pin
from datetime import datetime
#import Adafruit_DHT
from core import Database

def get_h_t() -> dict:
    hum, temp = 23.13123, 50.38293
    data = {"humidity": round(hum, 2), "temperature": round(temp, 2), "timestamp": __today()}
    push_to_csv(data)
    
    return data

def push_to_db(data:dict):
    return 

def push_to_csv(data:dict):
    fieldnames = ["humidity", "temperature", "timestamp"]
    csv_dir = "./static/csv/data.csv"
    with open(csv_dir, "a+", newline="") as file:
        for i in read_csv():
            if i["timestamp"] == data["timestamp"]:
                return
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow(data)
    return

def read_csv() -> list:
    csv_values = []
    with open("static/csv/data.csv", "r") as cf:
        csvreader = csv.DictReader(cf)
        for raw in csvreader:
            data = {"humidity": raw["humidity"], "temperature": raw["temperature"], "timestamp": raw["timestamp"]}
            csv_values.append(data)
    
    return csv_values

def __today() -> datetime:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")