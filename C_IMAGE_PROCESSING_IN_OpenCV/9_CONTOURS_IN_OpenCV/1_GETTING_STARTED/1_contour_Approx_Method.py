import numpy as np
import cv2

img = cv2.imread('bambou.jpeg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("NUMBER OF COUNTOURS = " +str(len(contours)))
print(contours[0])
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.drawContours(thresh, contours, -1, (0,255,0), 3)

#cv2.imshow('original',imgray)
cv2.imshow('img1Contours',img)
cv2.imshow('treshCountours',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows
