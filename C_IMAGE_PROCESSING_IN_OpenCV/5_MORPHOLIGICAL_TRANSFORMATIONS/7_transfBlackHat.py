import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(20,20))
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original',img)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()