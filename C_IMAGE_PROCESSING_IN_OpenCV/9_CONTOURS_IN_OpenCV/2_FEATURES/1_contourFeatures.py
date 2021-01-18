import cv2
import numpy as np

img = cv2.imread('nike.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,0)
image,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("NUMBER OF CONTOURS = " +str(len(contours)))
print(contours[0])


cnt = contours[0]
M = cv2.moments(cnt)
#print M

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print "area = ", cv2.contourArea(cnt)

print "perimeter = " ,cv2.arcLength(cnt,True)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.drawContours(img, contours, 0, (0,255,0), 3)
cv2.drawContours(thresh, contours, 0, (0,255,0), 3)


cv2.imshow('img1',img)


cv2.waitKey(0)
cv2.destroyAllWindows