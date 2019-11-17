import Adafruit_DHT
from CONFIG import pin
from database import DbClient
import time
from . import utcnow

db = DbClient().collection

sensor = Adafruit_DHT.DHT22
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def push_to_db():
    while True:
        data_h = {"humidity": humidity.round(2), "timestamp": utcnow}
        data_t = {"temperature": temperature.round(2), "timestamp": utcnow}

        db.update({"_id": 00}, {"$push": {"humidity": data_h}})
        db.update({"_id": 00}, {"$push": {"temperature": data_t}})
        
        time.sleep(3600)

