#!/usr/bin/env python3

# Created by Indraneel on 6/06/21
import cv2
from Camera import Camera



def main():
    camera = Camera("/dev/video2")
    camera.test_camera()

if __name__ == "__main__": main()