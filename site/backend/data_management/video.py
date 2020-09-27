from cv2 import cv2
import time

class Video(object):
    cameraTarg
    captureDev
    fps
    frameWidth
    frameHeight

    def __init__(self, target, fps):
        self.fps = fps
        self.cameraTarg = target 
        self.captureDev = cv2.VideoCapture(-1)
        self.record

    def __delete__(self):
        self.record.release()
        self.cap.release()
    
    def genCam(self):
        frame = self.encodeFrame(getFrame())
        socketio.emit("primaryStreamOut", frame)
        time.sleep(1/self.fps)
    
    def getFrame(self):
        _ret, frame = self.captureDev.read()
        _ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg  

    def encodeFrame(frame):
        return base64.b64encode(frame.tobytes()).decode('utf-8')

    def startWriting(self):
        caption = self.getFrame()
        self.record = cv2.VideoWriter('./temp/outputtedVideo.avi',cv2.VideoWriter_fourcc('M','J','P','G'), this.fps, (self.frameWidth,self.frameHeight))

    def stopWriting(self):
        self.record.release()

    def captureImage(self):
        tag = self.getFrame()

#new Video(-1)
#in dev it woudl be 0 and 1