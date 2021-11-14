from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.sensor_controller import api as sensor_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK is FRAMEWORK NGU NGOK',
          version='1.0',
          description='lala'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(sensor_ns, path='/sensor')
api.add_namespace(auth_ns)