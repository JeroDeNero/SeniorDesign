# from flask import Flask, render_template, Response, Blueprint
# import subprocess as sp
# import time

from . import socketio
from flask import Flask, render_template, request, Blueprint
import asyncio
import _thread
import time
from cv2 import cv2
import base64

count = 0
tagCount = 0
# video


@socketio.on('connect')
def on_connect():
    print('[INFO] WebClient connected.')
    global count
    if count == 0:
        _thread.start_new_thread(emitCams, ())
    count = count + 1


@socketio.on('disconnect')
def on_disconnect():
    print('[INFO] WebClient disconnected.')
    global count
    count = count - 1


@socketio.on('capture')
def capture():
    global video
    global tagCount

    if not (video == None):
        print('Captured Image')
        img = getFrame(video)
        cv2.imwrite('./temp/tag{}.jpeg'.format(tagCount), img)
        tagCount = tagCount + 1


# @socketio.on('startRecord')
# def record():

    # @bp.route('/videoFeed')
    # def videoFeed():
    #    return Response(gen(Camera()))


def emitCams():
    fps = 0.2
    global count
    #global video
    video = cv2.VideoCapture(-1)

    while count > 0:
        genMainCam(video, fps)

    video.release()


def genMainCam(video, fps):
    frame = encodeFrame(getFrame(video))
    socketio.emit("primaryStreamOut", frame)
    time.sleep(1/fps)


def getFrame(video):
    _ret, frame = video.read()
    _ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg


def encodeFrame(frame):
    return base64.b64encode(frame.tobytes()).decode('utf-8')


'''
async def genSecondCam():
    fps = 1

    while True:
        frame = Camera().getFrame()
        await asyncio.sleep(1/fps)
        print('emitting')
        socketio.emit("primaryStreamOut", frame)
'''
