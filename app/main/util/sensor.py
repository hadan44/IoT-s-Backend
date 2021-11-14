import Adafruit_DHT
from flask import jsonify
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

count = 10;

def dht11_sensor():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    if humidity is None and temperature is None:
        print("Sensor failure. Check wiring.");
        for x in range(count):
            print("Sensor failure. Check wiring.");
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                break

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(type(current_time))
    res = jsonify(
        humidity= humidity,
        temperature = temperature, 
        time = current_time
    )

    return res
