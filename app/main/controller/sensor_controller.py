from flask import Flask, Response, request
from flask_restplus import Resource

from ..util.sensor import dht11_sensor
from ..util.dto import SensorDto

api = SensorDto.api
_sensor = SensorDto.sensor 

@api.route('/dht11sensor')
class Sensor(Resource):
    @api.doc('get_data_sensor')

    def get(self):
        return dht11_sensor()