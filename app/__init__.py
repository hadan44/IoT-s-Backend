from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.sensor_controller import api as sensor_ns
from .main.controller.switch_controller import api as switch_ns
from .main.controller.remote_controller import api as remote_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'token'
    }
}

api = Api(blueprint,
          title='FLASK is FRAMEWORK NGU NGOK',
          version='2.0',
          description='lala',
          security= 'apiKey',
          authorizations=authorizations
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(sensor_ns, path='/sensor')
api.add_namespace(switch_ns)
api.add_namespace(remote_ns)
api.add_namespace(auth_ns)