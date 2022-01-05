from app.main.model.user import User
from ..service.blacklist_service import save_token
from app.main import Base, sessionLoader

class Auth:
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            print(data)
            session = sessionLoader()
            user = session.query(User).filter(User.username == str(data.get('username'))).first()
            print(user)
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.userID)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'userID': user.userID,
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'username or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        print(data)
        if data:
            auth_token = data
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                print('check1')
                return save_token(auth_token)
            else: 
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
            # get the auth token
            print(new_request)
            auth_token = new_request.headers.get('token')
            print(auth_token)
            if auth_token:
                resp = User.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    session = sessionLoader()
                    user = session.query(User).filter(User.userID==resp).first()
                    response_object = {
                        'status': 'success',
                        'data': {
                            'user_id': user.userID,
                            'username': user.username,
                            'password': user.password,
                            'location': user.location,
                            'emergency_phone': user.emergencyPhone,
                            'fullname': user.fullname
                        }
                    }
                    return response_object, 200
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401