import jwt
import datetime

from app.main.model.blacklist import BlacklistToken
from app.main import db, app

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    registered_on = db.Column(db.DateTime,  nullable=True)

    def __init__(self, id, username, password, registered_on):
        self.id = id
        self.username = username
        self.password = password
        self.registered_on = registered_on

    def check_password(self, password):
        if self.password == password: return True
        return False
        
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        print(app.config.get('SECRET_KEY'))
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=30),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            print(payload)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
