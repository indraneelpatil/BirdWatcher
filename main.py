#!/usr/bin/env python3

# Created by Indraneel on 6/06/21
import cv2
from Camera import Camera
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time

min_contour_area_pixels = 500 

def main():
    global min_contour_area_pixels
    camera = Camera("/dev/video2")
    #camera.test_camera()

    # initialize the first frame in the video stream
    firstFrame = None
    # loop over the frames of the video
    while True:
        # grab the current frame and initialize the occupied/unoccupied
        # text
        ret,frame = camera.handle.read()
    
        #frame = frame if args.get("video", None) is None else frame[1]
        text = "Unoccupied"
        # if the frame could not be grabbed, then we have reached the end
        # of the video
        if frame is None:
            break
        # resize the frame, convert it to grayscale, and blur it
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            # Skip first iteration
            continue
        ################################## Algorithm Start ####################################

        # compute the absolute difference between the current frame and
        # first frame
        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        cv2.imshow('frame', thresh)
        key = cv2.waitKey(1) & 0xFF
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < min_contour_area_pixels:
                continue
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"
            print("Occupied!")
        
        # if the `q` key is pressed, break from the lop
        if key == ord("q"):
            break
    camera.stop_camera()

if __name__ == "__main__": main()