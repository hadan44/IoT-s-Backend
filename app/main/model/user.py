import jwt
import datetime
import json

from app.main.model.blacklist import BlacklistToken
from app.main import db, app, sessionLoader, Base

class User(Base):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(20), index=True, nullable=False, , autoincrement=True)
    password = Column(db.String(20), nullable=False)
    registered_on = Column(db.DateTime,  nullable=True)

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
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            response = jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            ).decode('utf-8')
            print('payload: ', payload)
            print('token: ', type(response))
            return response
        except Exception as e:
            return str(e)

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), algorithm='HS256')
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
