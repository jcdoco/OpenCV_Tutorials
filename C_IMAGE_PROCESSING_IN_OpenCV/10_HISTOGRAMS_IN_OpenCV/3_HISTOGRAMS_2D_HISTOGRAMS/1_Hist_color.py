import cv2
import numpy as np

img = cv2.imread('image29resize.jpg')
img2 = cv2.imread('image29resize.jpg')
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)


hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])


cv2.imshow('img',img)
cv2.imshow('hsv',hsv)
cv2.imshow('hist',hist)
cv2.imshow('img2',img2)

cv2.waitKey(0)