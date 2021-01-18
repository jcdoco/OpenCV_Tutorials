import cv2 
import numpy as np


img = cv2.imread('test4.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imwrite('res.png',res)

cv2.imshow('equ',equ)
cv2.imshow('img',img)
cv2.imshow('hstack',res)
cv2.waitKey(0)