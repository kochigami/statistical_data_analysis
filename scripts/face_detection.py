#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
      
    scale = 4
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
    smallImg = cv2.resize(gray_image, (int (cv_image.shape[1] * 0.25), int(cv_image.shape[0] * 0.25)))
    smallImg = cv2.equalizeHist(smallImg)

    cascade_name = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_name)
    facerect = cascade.detectMultiScale(smallImg, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    if len(facerect) > 0:
      for rect in facerect:
        cv2.circle(cv_image, (int((rect[0] + rect[2] * 0.5) * scale), int((rect[1] + rect[2] * 0.5) * scale)), int(rect[2] * scale), (80, 80, 255), 3, 8, 0)
    cv2.imshow("Result Image", cv_image)
    cv2.waitKey(1)
    
def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
