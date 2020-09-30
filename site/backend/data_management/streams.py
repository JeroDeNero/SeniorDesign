# from flask import Flask, render_template, Response, Blueprint
# import subprocess as sp
# import time

from flask import Flask, render_template, request, Blueprint
from . import tempFileManger
from .video import Video
from . import socketio
from cv2 import cv2

import _thread
import asyncio
import base64
import time

count = 0
tagCount = 0

video = [None, None]


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

    if count < 1 and video[0] != None:
        del video[0]


@socketio.on('capture')
def capture(cam):
    global video
    global tagCount
    print(tagCount)

    if video[cam]:
        img = video[cam].getFrame()
        write = cv2.imwrite(
            'data_management/temp/tag{}.jpg'.format(tagCount), img)
        tagCount = tagCount + 1
        print('data_management/temp/tag{}.jpg'.format(tagCount))


@socketio.on('startRecording')
def startRecording():
    global video
    global tagCount
    tagCount = 0
    tempFileManger.clearAll()
    video[0].startWriting()


@socketio.on('endRecording')
def endRecording():
    global video
    video[0].stopWriting()


def emitCams():
    global count
    global video
    if (count > 0 and not video[0]):
        video[0] = Video(-1, 0.2)

    while count > 0:
        video[0].genCam()

    if count < 1:
        del video[0]
