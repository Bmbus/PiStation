import csv
from CONFIG import pin
from datetime import datetime
import Adafruit_DHT
from database import DbClient
from . import utcnow

db = DbClient().collection
sensor = Adafruit_DHT.DHT22


def get_h_t() -> dict:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    data = {"humidity": hum.round(2), "temperature": temp.round(2), "timestamp": utcnow()}
    push_to_db(hum, temp, utcnow())
    return data

def push_to_db(hum, temp, timestamp):
    push_data_hum = {"humidity": hum.round(2), "timestamp": utcnow()}
    push_data_temp = {"temperature": temp.round(2), "timestamp": utcnow()}
    db.update({"_id": 00}, {"$push": {"humidity": push_data_hum}})
    db.update({"_id": 00}, {"$push": {"temp": push_data_temp}})
    return