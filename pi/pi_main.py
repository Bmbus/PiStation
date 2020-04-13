from CONFIG import pin
from core.database import DbClient
import shedule
import Adafruit_DHT
from . import utcnow

db = DbClient().collection
sensor = Adafruit_DHT.DHT22

def push_to_db():
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)

    push_data_hum = {"humidity": hum.round(2), "timestamp": utcnow}
    push_data_temp = {"temperature": temp.round(2), "timestamp": utcnow}
    
    db.update({"_id": 00}, {"$push": {"humidity": push_data_hum}})
    db.update({"_id": 00}, {"$push": {"temp": push_data_temp}})

def get_data(): 
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    data = {"humidity": hum.round(2), "temperature": temp.round(2), "timestamp": utcnow}

    return data

if __name__ == "__main__":
    schedule.every().hour.do(push_to_db)

