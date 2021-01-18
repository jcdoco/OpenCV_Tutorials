import cv2
import numpy as np
img = cv2.imread('joker.jpeg',0)
higher_reso = cv2.pyrUp(img)
lower_reso = cv2.pyrDown(higher_reso)
higher_reso1 = cv2.pyrUp(lower_reso)



cv2.imshow('higher_reso',higher_reso)
cv2.imshow('lower_reso1',lower_reso)
cv2.imshow('higher_reso1',higher_reso1)

cv2.waitKey(0)
cv2.destroyAllWindows()