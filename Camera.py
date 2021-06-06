#!/usr/bin/env python3

# Created by Indraneel on 6/06/21
import cv2
import time

class Camera:

    def __init__(self,path):
        self.handle = cv2.VideoCapture(path)
        # Initialisation delay
        for i  in range(0,10):
            ret, frame = self.handle.read()
        #self.handle.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        #self.handle.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    def test_camera(self):
        while(True):
      
            # Capture the video frame
            # by frame
            ret, frame = self.handle.read()
        
            # Display the resulting frame
            cv2.imshow('frame', frame)
            
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Destroy all the windows
        cv2.destroyAllWindows()
        
    def stop_camera(self):
        
        # After the loop release the cap object
        self.handle.release()
