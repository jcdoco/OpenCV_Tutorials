import cv2
import numpy as np

img = cv2.imread('handWhite.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)




cnt = contours[0]
M = cv2.moments(cnt)
print M

mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
#pixelpoints = np.transpose(np.nonzero(mask))
pixelpoints = cv2.findNonZero(mask)
print pixelpoints

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)
mean_val = cv2.mean(imgray,mask = mask)
print mean_val


cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt,True)

k = cv2.isContourConvex(cnt)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

ellipse = cv2.fitEllipse(cnt)
h = (x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print h
img = cv2.ellipse(img,ellipse,(0,255,0),2)





cv2.imshow('img',img)

cv2.waitKey()










