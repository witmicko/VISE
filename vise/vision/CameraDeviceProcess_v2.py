import os

import atexit
import cv2
import time
from threading import Thread

from multiprocessing import Process,Pipe

from config.config import settings

from PyQt4 import QtCore, QtGui
from timeit import default_timer as timer

from vise.utils.VisionEmitter import VisionEmitter


class CameraDevice(Process):
    # video_signal = QtCore.pyqtSignal(QtGui.QImage)
    video_signal = 'data(PyQt_PyObject)'
    ui_preview = False

    def __init__(self, pipe):
        Process.__init__(self)
        atexit.register(self.release_cam)
        # self.transport = child_pipe
        self.emitter = VisionEmitter(pipe)
        self.emitter.daemon = True
        self.emitter.start()

        self.camera = cv2.VideoCapture(0)
        self.res_x = settings['camera']['res_x']
        self.res_y = settings['camera']['res_y']
        self.fps = settings['camera']['fps']
        self._id = settings['camera']['id']
        self.stopped = False
        self.set_resolution(self.res_x, self.res_y)
        self.set_framerate(self.fps)
        # self.buffer = []

    def __reduce__(self):
        return self.__class__, (self.emitter.pipe,)

    def emit_to_mother(self, signature, args=None):
        self.emitter.send(signature, args)

    def start_video(self):
        print("start video")
        while True:
            ret, image = self.camera.read()
            # ret, image = self.camera.read()
            # self.buffer.append(image)
            self.emit_to_mother('data(QImage)', image)
            time.sleep(0.01)
            if self.stopped:
                print("stopped")
                break

        print("releasing")
        self.camera.release

    def run(self):
        self.start_video()

    def release_cam(self):
        print("release_cam")
        # cc = cv2.VideoCapture(0)
        # dd = cc.release
        # self.stopped = True
        # print("release_cam2",dd)

    def get_pid(self):
        return os.getpid()



    def __str__(self):
        return 'Camera: ' \
               'id: {0._id}, ' \
               'res_x:{0.res_x}, ' \
               'res_y:{0.res_y}, ' \
               'fps: {0.fps} ' \
            .format(self)


    def get_framerate(self):
        """
        Reads currently set fps of the camera
        :return: currently set fps of the camera
        """
        return self.capture.get(cv2.CAP_PROP_FPS)

    def set_framerate(self, fps):
        """
        Sets fps of the camera device.
        note: not proved to work on webcam
        :param fps:
        :return:
        """
        self.camera.set(cv2.CAP_PROP_FPS, fps)

    def set_resolution(self, x, y):
        """
        Sets resolution of the camera
        :param x: horizontal res
        :param y: bertical res
        :return:
        """
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, x)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, y)

    def fps_test(self):
        # todo
        num_frames = 120
        print("Capturing {0} frames".format(num_frames))

        start = time.time()
        for i in range(0, num_frames):
            self.capture.read()
        end = time.time()

        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))

        fps = num_frames / seconds;
        print("Estimated frames per second : {0}".format(fps))
        self.capture.release()

    @QtCore.pyqtSlot()
    def preview_on(self):
        print("on")
        self.ui_preview = True

    @QtCore.pyqtSlot()
    def preview_off(self):
        print("off")
        self.ui_preview = False

    def capture(self):
        """
        captures frames into the video buffer, spawns new thread
        :return:
        """
        self.capture_thread = Thread(target=self.capture_in_thread())
        self.capture_thread.daemon = True
        self.capture_thread.start()
