import cv2
import numpy as np

img = cv2.imread('joker.jpeg')

cv2.imshow('original',img)
face = img[00:300,200:400]

cv2.imshow('face',face)


cv2.waitKey(0)

