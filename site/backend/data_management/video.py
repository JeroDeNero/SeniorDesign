# pylint: disable=no-member
"""to stop pylint from complainign about cv2"""

import base64
import time
import cv2

from data_management import socketio

VIDEOTYPE = 'mp4'
CODEC = 'avc1'


class Video(object):
    """object that contains all command each camera may need"""
    fps = None
    cameraTarg = None
    captureDev = None
    recording = False
    frameWidth = 640
    frameHeight = 480
    recordTime = time.time()

    def __init__(self, target, fps):
        self.fps = fps
        self.cameraTarg = target
        self.captureDev = cv2.VideoCapture(target)
        self.frameWidth = int(self.captureDev.get(3))
        self.frameHeight = int(self.captureDev.get(4))

    def __delete__(self, instance):
        self.record.release()
        self.captureDev.release()

    def genCam(self):
        frame = self.getFrame()
        if self.recording:
            self.writeVid(frame)
        else:
            time.sleep(1/self.fps)

        frame = self.encodeFrame(self.toJPG(frame))
        socketio.emit("primaryStreamOut", frame)

    def getFrame(self):
        _ret, frame = self.captureDev.read()
        return frame

    def toJPG(self, frame):
        _ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg

    def encodeFrame(self, frame):
        return base64.b64encode(frame.tobytes()).decode('utf-8')

    def startWriting(self):
        global CODEC
        global VIDEOTYPE

        cv2.imwrite('data_management/temp/imageFront.jpg', self.getFrame())
        fourcc = cv2.VideoWriter_fourcc(*CODEC)
        self.record = cv2.VideoWriter('data_management/temp/outputtedVideo.{}'.format(VIDEOTYPE),
                                      fourcc, 
                                      self.fps, 
                                      (self.frameWidth, self.frameHeight))
        self.recording = True

    def writeVid(self, frame):
        self.record.write(frame)

    def stopWriting(self):
        self.recording = False
        self.record.release()

    def captureImage(self):
        return self.getFrame()

# new Video(-1)
# in dev it would be 0 and 1
