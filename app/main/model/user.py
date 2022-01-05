import jwt
import datetime
import json

from app.main.model.blacklist import BlacklistToken
from app.main import db, app, sessionLoader, Base
from sqlalchemy import Table, Column, Float, Integer, String, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    userID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    emergencyPhone = Column(String(20), nullable=True)
    location = Column(String(50), nullable=True)
    fullname = Column(String(100), nullable=True)

    def __init__(self, userID, username, password, emergencyPhone, location, fullname):
        self.userID = userID
        self.username = username
        self.password = password
        self.emergencyPhone = emergencyPhone
        self.location = location
        self.fullname = fullname

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
