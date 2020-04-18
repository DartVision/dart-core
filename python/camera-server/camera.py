from time import sleep
from io import BytesIO
from threading import Thread, Lock
from picamera import PiCamera
import copy
import logging


class Camera(object):
    def __init__(self):
        self._camera = PiCamera()
        self._camera.resolution = (3280, 2464)
        self._camera.start_preview()
        self._image = None
        self._lock = Lock()
        self._thread = Thread(target=self._start_capture)
        # Camera warm-up time
        sleep(2)
        self._thread.start()

    def capture(self):
        self._lock.acquire()
        image = copy.copy(self._image)
        self._lock.release()
        return image

    def _start_capture(self):
        while True:
            buffer = BytesIO()
            self._camera.capture(buffer, format='jpeg', quality=100)
            buffer.seek(0)
            self._lock.acquire()
            self._image = buffer.read()
            self._lock.release()
