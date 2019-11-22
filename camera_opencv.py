import os
import cv2
from base_camera import BaseCamera
from func import contorno2

class Camera(BaseCamera):
    video_source = 0

    def __init__(self, video_source='video_original.avi'):
        # BaseCamera.thread=None
        Camera.set_video_source(video_source)
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        alfa = 0 # alfa é o limiar de angulo para que apareça um contorno
        count = 0
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            img = contorno2(img, alfa)
            count+=1
            # encode as a jpeg image and return it
            if img is None:
                break
            yield cv2.imencode('.jpg', img)[1].tobytes()
