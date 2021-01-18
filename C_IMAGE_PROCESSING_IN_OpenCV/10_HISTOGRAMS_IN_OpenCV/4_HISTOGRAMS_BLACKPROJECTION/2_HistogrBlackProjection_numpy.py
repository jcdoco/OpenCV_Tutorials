import cv2
import numpy as np
roi = cv2.imread('federerElem.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#target is the image we search in
target = cv2.imread('federer_resize.jpg')
cv2.imshow('target',target)
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
print(M)
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
h,s,v = cv2.split(hsvt)
#Italics are self imposed
R=M/I
print(R.shape)
B = R[h.ravel(),s.ravel()]
print(B)
B = np.minimum(B,1)
print(B)
B = B.reshape(hsvt.shape[:2])
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
B=cv2.filter2D(B,-1,disc)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)
cv2.imshow('B',B)
ret,thresh = cv2.threshold(B,2,255,0)
cv2.imshow('thresh',thresh)
res = cv2.bitwise_and(target,target,mask=thresh)
cv2.imshow('res',res)
cv2.waitKey(0)