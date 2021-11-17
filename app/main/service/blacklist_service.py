from app.main import session
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        session.add(blacklist_token)
        session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200