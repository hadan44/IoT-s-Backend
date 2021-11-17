import Adafruit_DHT
from flask import jsonify
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

count = 5;

def dht11_sensor():
    _humidity, _temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if _humidity is not None and _temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(_temperature, _humidity))
    if _humidity is None and _temperature is None:
        print("Sensor failure. Check wiring.");
        for x in range(count):
            print("Sensor failure. Check wiring.");
            _humidity, _temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if _humidity is not None and _temperature is not None:
                break
            time.sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(_humidity)
    print(_temperature)
    res = jsonify(
        humidity= _humidity,
        temperature = _temperature, 
        time = current_time
    )
    return res
