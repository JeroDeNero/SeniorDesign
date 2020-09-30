from . import socketio
from cv2 import cv2

import time
import base64


class Video(object):
    fps = None
    cameraTarg = None
    captureDev = None
    recording = False
    frameWidth = 640
    frameHeight = 480

    def __init__(self, target, fps):
        print(target)
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

        frame = self.encodeFrame(self.toJPG(frame))
        socketio.emit("primaryStreamOut", frame)
        time.sleep(1/self.fps)

    def getFrame(self):
        _ret, frame = self.captureDev.read()
        return frame

    def toJPG(self, frame):
        _ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg

    def encodeFrame(self, frame):
        return base64.b64encode(frame.tobytes()).decode('utf-8')

    def startWriting(self):
        cv2.imwrite('data_management/temp/imageFront.jpg', self.getFrame())
        self.record = cv2.VideoWriter('data_management/temp/outputtedVideo.avi',
                                      cv2.VideoWriter_fourcc(*'MJPG'), 1, (self.frameWidth, self.frameHeight))
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
