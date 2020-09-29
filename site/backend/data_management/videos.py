'''

ds_factor = 0.6


class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(-1)

    def __del__(self):
        self.video.release()

    def getFrame(self):
        _ret, frame = self.video.read()
        _ret, jpeg = cv2.imencode('.jpg', frame)
        return base64.b64encode(jpeg.tobytes()).decode('utf-8')
'''
