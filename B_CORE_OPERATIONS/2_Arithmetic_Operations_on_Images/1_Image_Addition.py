import cv2

img1 = cv2.imread('a.jpg')
cv2.imshow('img1', img1)

img2 = cv2.imread('b.jpg')
cv2.imshow('img2', img2)

img = cv2.add(img1,img2)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.distroyAllWindows()