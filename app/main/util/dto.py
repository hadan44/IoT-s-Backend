from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer(required=True, description='user id'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class SensorDto:
    api = Namespace('sensor', description='sensor related operations')
    sensor = api.model('sensor', {
        'temperature': fields.Float(required=True, description='temperature from DHT11 sensor'),
        'humidity': fields.Float(required=True, description='humidity from DHT11 senor'),
        'time': fields.String(required=True, description='Time sensor record'),
    })

class SwitchDto:
    api = Namespace('switch', description='switch related operations')
    switch = api.model('switch', {
        'slot': fields.Integer(required=True, description='switch slot'),
        'data': fields.Boolean(required=True, description='Input data'),
    })
