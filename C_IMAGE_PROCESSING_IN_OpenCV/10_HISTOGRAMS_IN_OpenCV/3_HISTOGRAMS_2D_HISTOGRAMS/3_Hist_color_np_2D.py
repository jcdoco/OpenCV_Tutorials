

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('joker.jpeg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
print (hist)
cv2.imshow('hist', hist)
cv2.waitKey(0)
