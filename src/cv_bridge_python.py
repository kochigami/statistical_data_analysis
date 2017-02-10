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
    self.image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Origin Image", cv_image)
    cv2.waitKey(3)
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Gray Image", gray_image)
    cv2.waitKey(3)
    cascade_name = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_name)
    facerect = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    if len(facerect) > 0:
      for rect in facerect:
        print rect
        cv2.rectangle(cv_image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (255, 255, 255), thickness=2) ## ??
    cv2.imshow("Result Image", cv_image)
    cv2.waitKey(3)
    
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
