#!/usr/bin/python# -*- coding utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("0.jpg")

# 灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, bin = cv2.threshold(img_gray, 160, 255, 0)
img_gray = cv2.medianBlur(bin, 3)

cv2.imshow("test", img_gray)
cv2.waitKey(10000)