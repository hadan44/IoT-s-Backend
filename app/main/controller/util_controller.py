from flask import Flask, Response, request
from flask_restplus import Resource

from ..util.picam import VideoCamera
from ..util.sensor import dht11_sensor

pi_camera = VideoCamera(flip=False)

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@api.route('/videofeed')
class Camera(Resource):
    def get(self):
        return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@api.route('/dht11sensor')
class Camera(Resource):
    def get(self):
        return dht11_sensor()

