import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 2
h,t = Adafruit_DHT.read_retry(sensor, pin)

print(f"Humidity: {round(h, 2)}%")
print(f"Temperature: {round(t, 2)}C°")
