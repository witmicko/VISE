import os

import cv2
import time
from threading import Thread

from config.config import settings

from PyQt4 import QtCore, QtGui


class CameraDevice(QtCore.QObject):
    video_signal = QtCore.pyqtSignal(QtGui.QImage)
    ui_preview = False


    def __init__(self, parent=None):
        super(CameraDevice, self).__init__(parent)
        self.camera = cv2.VideoCapture(0)
        self.res_x = settings['camera']['res_x']
        self.res_y = settings['camera']['res_y']
        self.fps = settings['camera']['fps']
        self._id = settings['camera']['id']
        self.capture = cv2.VideoCapture(self._id)
        self.set_resolution(self.res_x, self.res_y)
        self.set_framerate(self.fps)
        self.buffer = []

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
    def startVideo(self):

        run_video = True
        while run_video:
            # print("frame")
            ret, image = self.camera.read()
            self.buffer.append(image)

            if self.ui_preview:
                color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                height, width, _ = color_swapped_image.shape

                qt_image = QtGui.QImage(color_swapped_image.data,
                                        width,
                                        height,
                                        color_swapped_image.strides[0],
                                        QtGui.QImage.Format_RGB888)

                self.video_signal.emit(qt_image)
            time.sleep(0.3)

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

