import datetime
from app.main import sessionLoader, Base
from flask import Response
from app.main.model.user import User
from ..service.switch_service import save_switch_name

def save_new_user(data):
    session = sessionLoader()
    user = session.query(User).filter(User.username == str(data['username'])).first()
    if not user:
        new_user = User(
            userID=data['userID'],
            username=data['username'],
            password=data['password'],
            emergencyPhone='0396302198',
            location='hanoi',
            fullname='Nguyen Vuong Tien'
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def modify_user(data):
    session = sessionLoader()
    save_switch_name(data)
    session.query(User).filter(User.userID == int(data['userID'])).update({User.password:str(data['password']), User.fullname:str(data['fullname']), User.emergencyPhone:str(data['emergencyPhone']), User.location:str(data['location'])}, synchronize_session = False)
    session.commit()
    return 1

def get_all_users():
    session = sessionLoader()
    result = session.query(User).all()
    return result


def get_a_user(public_id):
    session = sessionLoader()
    return session.query(User).filter(User.userID==public_id).first()


def save_changes(data):
    session = sessionLoader()
    session.add(data)
    session.commit()