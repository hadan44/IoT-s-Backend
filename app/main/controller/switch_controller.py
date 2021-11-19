from flask import request
from flask_restplus import Resource

from app.main.service.switch_service import send_data_to_switch, get_last_state
from app.main.util.decorator import token_required
from ..util.dto import SwitchDto

api = SwitchDto.api
_switch = SwitchDto.switch

@api.route('/' , methods=['POST'])
class Switch(Resource):
    @api.doc('switch_control')
    @api.expect(_switch, validate=True)
    @token_required
    def post(self):
        # get the post data
        post_data = request.json
        return send_data_to_switch(post_data)

@api.route('/laststate' , methods=['GET'])
class Switch(Resource):
    @api.doc('get_switch_last_state')
    @token_required
    def get(self):
        return get_last_state()

