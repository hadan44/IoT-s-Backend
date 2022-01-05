from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'userID': fields.Integer(required=True, description='user id'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'emergencyPhone': fields.String(required=True, description='user password'),
        'location': fields.String(required=True, description='user password'),
        'fullname': fields.String(required=True, description='user password'), 
    })
    user_and_sw = api.model('user', {
        'userID': fields.Integer(required=True, description='user id'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'emergencyPhone': fields.String(required=True, description='user password'),
        'location': fields.String(required=True, description='user'),
        'fullname': fields.String(required=True, description='user'),
        'name1':  fields.String(required=True, description='user'),
        'name2':  fields.String(required=True, description='user '),
        'name3':  fields.String(required=True, description='user'),
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
        'out1': fields.Integer(required=True, description='Input data'),
        'out2': fields.Integer(required=True, description='Input data'),
        'out3': fields.Integer(required=True, description='Input data'),
    })

class RemoteDto:
    api = Namespace('remote', description='remote related operations')
    remote_create = api.model('remote_create', {
        'remote_name': fields.String(required= True, description='Input data'),
        'command': fields.List(fields.String, required= True, description='Input data')
    })
    remote_send = api.model('remote_send', {
        'remote_name': fields.String(required= True, description='Input data'),
        'command': fields.String(required= True, description='Input data')
    }) 

class CameraDto:
    api = Namespace('camera', description='camera related operations')
    
