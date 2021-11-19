import Adafruit_DHT
from flask import jsonify
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

count = 2;

def dht11_sensor():
    _humidity, _temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if _humidity is None and _temperature is None:
        for x in range(count):
            _humidity, _temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if _humidity is not None and _temperature is not None:
                break
            time.sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    response_object = {
        'status': 'success',
        'data': {
            'humidity': _humidity,
            'temperature': _temperature, 
            'time': current_time
        }
    }
    return response_object , 201
