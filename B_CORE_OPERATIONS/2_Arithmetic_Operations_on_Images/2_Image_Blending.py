import cv2

img1 = cv2.imread('a.jpg')
cv2.imshow('img1', img1)

img2 = cv2.imread('b.jpg')
cv2.imshow('img2', img2)

fusion = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('fusion',fusion)


cv2.waitKey(0)
cv2.distroyAllWindows()