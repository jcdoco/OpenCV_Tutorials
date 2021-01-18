import cv2
import numpy as np

widht , height = 578, 350
img = cv2.imread('etoiles de david.png',0)
img1 = cv2.resize(img,(widht,height))
cv2.imwrite('star_david_resize.png',img1)


img1 = cv2.imread('4branches_resiz.png',0)
img2 = cv2.imread('star_david_resize.png',0)
cv2.imshow('starDavid.png',img2)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
image,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
image,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret

cv2.waitKey(0)
