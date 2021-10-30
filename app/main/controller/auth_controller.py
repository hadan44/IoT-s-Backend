from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login' , methods=['POST'])
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(post_data)


@api.route('/logout',  methods=['POST'])
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('token')
        print("token", auth_header)
        return Auth.logout_user(auth_header)