# pylint: disable=no-member
"""to stop pylint from complainign about cv2"""

import _thread
import time
import cv2
import os

from dotenv import load_dotenv

from data_management import tempFileManger
from data_management.video import Video
from data_management import socketio


COUNT = 0
TAGCOUNT = 0
REBOOT = False
VIDEO = []


@socketio.on('connect')
def on_connect():
    print('[INFO] WebClient connected.')
    global COUNT
    if COUNT == 0:
        time.sleep(1)
        _thread.start_new_thread(emitCams, ())
    COUNT = COUNT + 1


@socketio.on('disconnect')
def on_disconnect():
    print('[INFO] WebClient disconnected.')
    global COUNT
    COUNT = COUNT - 1


@socketio.on('capture')
def capture(cam):
    global VIDEO
    global TAGCOUNT

    if (COUNT > 0 and 0 not in VIDEO):
        img = VIDEO[cam].getFrame()
        cv2.imwrite('data_management/temp/tag{}.jpg'.format(TAGCOUNT), img)

        timerCapture = VIDEO[cam].getTime()

        # location Request
        # send frontend details

        socketio.emit("addTag",
                      {"Position": TAGCOUNT,
                       "Lat": 0,
                       "Longi": 0,
                       "VideoTime": timerCapture})

        TAGCOUNT = TAGCOUNT + 1

@socketio.on('refocus')
def refocus():
    global VIDEO

    for item in VIDEO:
        item.refocus()

@socketio.on('startRecording')
def startRecording():
    global VIDEO
    global TAGCOUNT
    TAGCOUNT = 0
    tempFileManger.clearAll()
    VIDEO[0].startWriting()


@socketio.on('endRecording')
def endRecording():
    global VIDEO
    VIDEO[0].stopWriting()


def emitCams():
    global COUNT
    global VIDEO

    if (COUNT > 0 and 0 not in VIDEO):
        REBOOT = False
        os.environ.pop('MAIN_FPS')
        os.environ.pop('SECONDARY_FPS')
        load_dotenv("data_management/../.env")
        VIDEO.insert(0, Video(-1, int(os.environ.get("MAIN_FPS")), 0, False))

    while COUNT > 0 and 0 not in VIDEO and not REBOOT:
        VIDEO[0].genCam()

    del VIDEO[0]
    VIDEO = []

    if COUNT > 0:
        emitCams()


def rebootStream():
    global REBOOT
    REBOOT = True
