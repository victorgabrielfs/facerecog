import cv2
from imutils.video import WebcamVideoStream


class VideoCamera(object):

    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image = self.stream.read()

        detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        face = detector.detectMultiScale(image, 1.1, 7)
        for (x, y, h, w) in face:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        data = []
        data.append(jpeg.tobytes())
        return data


def gen(camera):
    while True:
        data = camera.get_frame()

        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

