from app.main import sessionLoader
from app.main.model.remoteCommand import Remote
import json
from sqlalchemy import distinct
import lirc

def save_new_remote(data):
    command_arr = []
    counterr = 1
    session = sessionLoader()
    countid = session.query(Remote.id).count()
    for _command in data['command']:
        print(data['remote_name'])
        print(_command)
        remote = session.query(Remote).filter(Remote.command == _command, Remote.remote_name == data['remote_name']).first()
        if not remote:
            countid+=1
            new_remote_command = Remote(
                id = int(countid),
                command = _command,
                remote_name = data['remote_name']
            )
            counterr+=1
            command_arr.append(new_remote_command)
        else:
            res = {
                'status': 'fail',
                'message': 'Command already exists in line  ' + str(counterr) + '. Please try again.',
            }
            response_object = json.dumps(res)
            return response_object, 409

    for new_command in command_arr:
        save_changes(new_command)

    response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
    }
    return response_object, 201
    
def get_all_remote_name():
    session = sessionLoader()
    remote_name_list = session.query(distinct(Remote.remote_name))
    characters_to_remove = "'(),"
    res = []
    for x in remote_name_list:
        newstring = str(x)
        for character in characters_to_remove:
            newstring = newstring.replace(character, "")
        res.append(newstring)
    response_object = {
        'status': 'success',
        'data': res
    }
    return response_object, 200


def send_remote_signal(data):
    key = data['command']
    remote = data['remote_name']
    client = lirc.Client()
    try:
        client.send_once(remote, key)
    except lirc.exceptions.LircdCommandFailureError as error:
        print('Unable to send key!')
        print(error)
        response_object = {
            'status': 'Fail',
            'message': error
        }
        return response_object, 409

    response_object = {
            'status': 'success',
            'message': 'Successfully sended.'
    }
    return response_object, 200

def get_remote_by_name(remote_name):
    session = sessionLoader()
    remote = session.query(Remote.command).filter(Remote.remote_name == remote_name).all()
    print(remote)
    res = []
    for x in remote:
        res.append(x[0])
    print(res)
    response_object = {
        'status': 'success',
        'data': res
    }
    return response_object

def save_changes(data):
    session = sessionLoader()
    session.add(data)
    session.commit()