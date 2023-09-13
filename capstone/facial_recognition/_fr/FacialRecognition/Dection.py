import numpy as np
import cv2 as cv


class Detector:
    def __init__ (self,use_cuda = False):
        #import model
        self.faceModel = cv.dnn.readNetFromCaffe("models/res10_300x300_ssd_iter_140000.prototxt",
        caffeModel="models/res10_300x300_ssd_iter_140000.caffemodel")

        #USE GPU Aceleration:
        if use_cuda:
            self.faceModel.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
            self.faceModel.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

    def processImage(self,imgName):
        self.img = cv.imread(imgName)
        (self.height, self.width) = self.img.shape[:2]
        self.processFrame()
        cv.imshow("Output", self.img)
        cv.waitKey(0)

    def processVideo(self, videoName, webcam=False):
        cap = cv.VideoCapture(videoName)
        if webcam:
            cap = cv.VideoCapture(0)
        if (cap.isOpened() == False):
            print("Unable to load video")
            return
        (sucess, self.img) = cap.read()
        (self.height, self.width) = self.img.shape[:2]

        while sucess:
            self.processFrame()
            cv.imshow("Output", self.img)
            key=cv.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            (sucess, self.img) = cap.read()

        cap.release()
        cv.destroyAllWindows()

    def processFrame(self):
        blob = cv.dnn.blobFromImage(self.img, 1.0, (300,300), (104.0, 177.0, 123.0),
        swapRB = False, crop = False)
        self.faceModel.setInput(blob)
        pred = self.faceModel.forward()

        for i in range(0, pred.shape[2]):
            if pred[0,0,i,2] > 0.5:
                box = pred[0,0,i,3:7] * np.array([self.width, self.height, self.width, self.height])
                (xmin, ymin, xmax, ymax) = box.astype("int")
                cv.rectangle(self.img, (xmin, ymin), (xmax, ymax), (0,255,0), 2)
