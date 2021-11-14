from flask import Flask, render_template, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .util.picam import VideoCamera
#from models import User, BlacklistToken

app = Flask(__name__)
# app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/iot_mobile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'b\xe1\xfa\xd8h\xa9$\xfax\xad\xb1mS\xb4\x17k\x89'

db = SQLAlchemy(app)
CORS(app)

pi_camera = VideoCamera(flip=True)

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run()

def create_app(config_name):
    return app