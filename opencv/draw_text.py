#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("test.png", 1)

height = img.shape[0]
width = img.shape[1]
print height
print width

fontType = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "SAMPLE_TEXT", (width/4, height/2), fontType, 2, (0, 0, 0), 3, cv2.CV_AA)

# 画像を表示
cv2.namedWindow("draw_text_test", cv2.WINDOW_NORMAL)
cv2.imshow("draw_text_test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
