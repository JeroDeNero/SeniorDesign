import os

from data_management import socketio
from data_management import roboto


@socketio.on('binary')
def binary(state):
    if ('binary' in os.environ):
        os.environ.pop('binary')

    os.environ['binary'] = state


@socketio.on('stop')
def stop():
    if ('stop' in os.environ):
        os.environ.pop('stop')

    os.environ['stop'] = 'True'
    roboto.stopMotor()


@socketio.on('stopCam')
def stopCam(target):
    if ('stop' in os.environ):
        os.environ.pop('stop')

    os.environ['stop'] = 'True'
    socketio.start_background_task(roboto.stopCamera(target))


@socketio.on('speed')
def speed(state):
    if ('speed' in os.environ):
        os.environ.pop('speed')

    os.environ['speed'] = str(state)


@socketio.on('movement')
def movement(state, value):
    if ('movement' in os.environ):
        os.environ.pop('movement')

    if ('movementVal' in os.environ):
        os.environ.pop('movementVal')

    os.environ['movement'] = state
    os.environ['movementVal'] = str(value)

    if state == 'straight':
        socketio.start_background_task(roboto.moveStraight(value))
    else:
        socketio.start_background_task(roboto.rotate(value))


@socketio.on('camera')
def camera(state, value):
    if ('camera' in os.environ):
        os.environ.pop('camera')

    if ('cameraVal' in os.environ):
        os.environ.pop('cameraVal')

    os.environ['camera'] = state
    os.environ['cameraVal'] = str(value)

    socketio.start_background_task(roboto.moveCamera(state, value))


@socketio.on('camHolt')
def camHolt():
    socketio.start_background_task(roboto.holdCamera())
