from time import sleep
from io import BytesIO
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self._camera = PiCamera()
        self._camera.resolution = (3280, 2464)
        self._camera.start_preview()
        # Camera warm-up time
        sleep(2)

    def capture(self):
        buffer = BytesIO()
        self._camera.capture(buffer, format='jpeg', quality=100)
        buffer.seek(0)
        return buffer.read()


if __name__ == '__main__':
    import time

    camera = Camera()
    t0 = time.time_ns()
    x = camera.capture()
    t1 = time.time_ns()
    print((t1 - t0) / 1000000)
