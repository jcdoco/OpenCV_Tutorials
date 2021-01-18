import cv2
import numpy as np

img = cv2.imread('cropped_im17.jpg')
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

#x,y,w,h = cv2.boundingRect(cnt)
#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#cv2.imshow('1',img)

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('img',img)

cv2.waitKey()










