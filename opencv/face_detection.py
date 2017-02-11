#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import numpy as np

def face_detection():
    scale = 4
    cap = cv2.VideoCapture(0)

    while(True):
        # ret: flag on succeeding obtaining a frame
        ret, frame = cap.read()
        gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        smallImg = cv2.resize(gray_image, (int (frame.shape[1] * 0.25), int(frame.shape[0] * 0.25)))
        smallImg = cv2.equalizeHist(smallImg)

        cascade_name = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
        cascade = cv2.CascadeClassifier(cascade_name)
        facerect = cascade.detectMultiScale(smallImg, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        if len(facerect) > 0:
            for rect in facerect:
                cv2.circle(frame, (int((rect[0] + rect[2] * 0.5) * scale), int((rect[1] + rect[2] * 0.5) * scale)), int(rect[2] * scale), (80, 80, 255), 3, 8, 0)
                
        cv2.imshow("Result Image", frame)
        cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()

if __name__ == '__main__':
    try:
        face_detection()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()
