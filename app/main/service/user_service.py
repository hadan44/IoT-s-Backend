import uuid
import datetime

from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        new_user = User(
            id=data['id'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
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

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()