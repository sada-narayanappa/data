
import sys
from Dection import *


#
def Detect():
    #Initial Face Detection in image and video
    detector = Detector(use_cuda=True)
    detector.processImage("DetectorFiles/Aran1.jpg")
    detector.processVideo("DetectorFiles/AranMariaVideo.mp4")
    detector.processVideo(None,webcam=True)


def main():
    if "detect" in sys.argv:
        Detect()

if __name__ == "__main__":

    main()
