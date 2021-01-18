import numpy as np
import cv2

img2 = cv2.imread('test3.jpg',0)
img = cv2.imread('test3.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res = np.hstack((img2,cl1)) #stacking images side-by-side

#cv2.imwrite('clahe_2.jpg',cl1)


cv2.imshow('res',res)

cv2.waitKey(0)