from app.main import sessionLoader
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    session = sessionLoader()
    print('check2')
    countid = session.query(BlacklistToken.id).count()
    print(countid)
    blacklist_token = BlacklistToken(countid + 1, token)
    print(blacklist_token)
    session.add(blacklist_token)
    session.commit()
    # try:
    #     # insert the token
        
    response_object = {
        'status': 'success',
        'message': 'Successfully logged out.'
    }
    return response_object, 200
    # except Exception as e:
    #     response_object = {
    #         'status': 'fail',
    #         'message': e
    #     }
    #     return response_object, 200