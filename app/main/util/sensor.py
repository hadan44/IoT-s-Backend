import Adafruit_DHT
import json
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def dht11_sensor():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    res = {
        "humidity": humidity,
        "temperature": temperature, 
        "time": current_time
    }

    return json.dumps(res)
