import cv2
import numpy as np

img = cv2.imread('handWhite.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cnt = contours[0]
M = cv2.moments(cnt)
print M


cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt,True)

k = cv2.isContourConvex(cnt)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

x,y,w,h = cv2.boundingRect(cnt)
b = aspect_ratio = float(w)/h
print b

rect_area = w*h
extent = float(area)/rect_area
print extent

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print str

equi_diameter = np.sqrt(4*area/np.pi)
print equi_diameter

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)




#cv2.imshow('1',img)


rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,255,0),2)

cv2.imshow('img',img)

cv2.waitKey()










