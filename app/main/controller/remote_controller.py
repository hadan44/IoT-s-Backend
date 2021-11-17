from flask import request
from flask_restplus import Resource

from app.main.service.remote_service import save_new_remote, get_all_remote_name, send_remote_signal
from ..util.dto import RemoteDto

api = RemoteDto.api
_remote = RemoteDto.remote_create
_send = RemoteDto.remote_send

@api.route('/createremote' , methods=['POST'])
class Remote(Resource):
    @api.doc('create_remote')
    @api.expect(_remote, validate=True)
    def post(self):
        post_data = request.json
        return save_new_remote(post_data)

@api.route('/' , methods=['POST'])
class Remote(Resource):
    @api.doc('send_remote_signal')
    @api.expect(_send, validate=True)
    def post(self):
        post_data = request.json
        return send_remote_signal(post_data)

@api.route('/getallremotename' , methods=['GET'])
class Remote(Resource):
    @api.doc('get_switch_last_state')
    def get(self):
        return get_all_remote_name()