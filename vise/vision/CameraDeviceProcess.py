import os

import cv2
import time
from threading import Thread

from multiprocessing import Process

from config.config import settings

from PyQt4 import QtCore, QtGui


class CameraDevice(Process):
    # video_signal = QtCore.pyqtSignal(QtGui.QImage)
    video_signal = 'data(PyQt_PyObject)'
    ui_preview = False

    def __init__(self, transport, queue, daemon=True):
        Process.__init__(self)
        self.daemon = daemon
        self.transport = transport
        self.data_from_mother = queue

        # self.camera = cv2.VideoCapture(0)
        self.res_x = settings['camera']['res_x']
        self.res_y = settings['camera']['res_y']
        self.fps = settings['camera']['fps']
        self._id = settings['camera']['id']

        # self.set_resolution(self.res_x, self.res_y)
        # self.set_framerate(self.fps)
        self.buffer = []

    def emit_to_mother(self, signature, args=None):
        self.transport.send((signature, args))

    def start_video(self):
        camera = cv2.VideoCapture(0)
        run_video = True
        while run_video:
            ret, image = camera.read()
            self.buffer.append(image)

            self.emit_to_mother('data(QImage)', image)

    def run(self):
        self.start_video()

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
        self.capture.set(cv2.CAP_PROP_FPS, fps)

    def set_resolution(self, x, y):
        """
        Sets resolution of the camera
        :param x: horizontal res
        :param y: bertical res
        :return:
        """
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, x)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, y)

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
