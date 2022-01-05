from flask import request
from flask_restplus import Resource
from app.main.util.decorator import token_required

from app.main.util.dto import UserDto
from app.main.service.user_service import save_new_user, get_all_users, get_a_user, modify_user

api = UserDto.api
_user = UserDto.user
_user_and_sw = UserDto.user_and_sw

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    @token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(200, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        print(data)
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get an user')
    @api.marshal_with(_user)
    @token_required
    def get(self, public_id):
        """get a user given id"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

@api.route('/adjust')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('modify an user')
    @api.expect(_user_and_sw, validate=True)
    @token_required
    def post(self):
        data = request.json
        print(data)
        return modify_user(data)
        