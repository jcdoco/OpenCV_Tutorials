import cv2
import numpy as np


img1 = cv2.imread('a.jpg')
img2 = cv2.imread('b.jpg')

bit_and = cv2.bitwise_and(img1,img2)
cv2.imshow('bit_and',bit_and)
cv2.imwrite('Picture_style_JC_1.jpg',bit_and)

bit_or = cv2.bitwise_or(img1,img2)
cv2.imshow('bit_or',bit_or)
cv2.imwrite('Picture_style_JC_2.jpg',bit_or)

bit_xor = cv2.bitwise_xor(img1,img2)
cv2.imshow('bit_xor',bit_xor)
cv2.imwrite('Picture_style_JC_3.jpg',bit_xor)

bit_not = cv2.bitwise_not(img1,img2)
cv2.imshow('bit_nor',bit_not)
cv2.imwrite('Picture_style_JC_4.jpg',bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()