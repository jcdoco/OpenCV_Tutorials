import cv2
import numpy as np

img = cv2.imread('handWhite.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
image,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(c) for c in contours]
final = cv2.drawContours(img, hull, 0, (255,255,255))



cv2.imshow('1',img)
cv2.imshow('2',thresh)


cv2.waitKey(0)
cv2.destroyAllWindows