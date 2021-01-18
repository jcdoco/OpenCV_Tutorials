import cv2
import numpy as np


widht , height = 578, 350
img = cv2.imread('4branches.png')
img1 = cv2.resize(img,(widht,height))
cv2.imwrite('4branches_resiz.png',img1)

img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
image, contours,hierarchy = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img1,start,end,[0,255,0],2)
    cv2.circle(img1,far,5,[0,0,255],-1)

cv2.imshow('img',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()