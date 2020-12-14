import cv2
import numpy as np
widht, height = 578, 350
widht1, height1 = 289, 175
a = cv2.imread('a.jpg')
b = cv2.resize(a,(widht,height))
c = cv2.resize(b,(widht1,height1))
b[0:175,289:578] = c
cv2.imshow('b',b)
cv2.waitKey(0)
cv2.destroyAllWindows