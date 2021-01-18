import cv2
img = cv2.imread('joker.jpeg')
img_level_1 = cv2.pyrDown(img)
img_level_2 = cv2.pyrDown(img_level_1)

cv2.imshow('img',img)
cv2.imshow('img2',img_level_1)
cv2.imshow('img3',img_level_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
