import cv2
import numpy as numpy


width, height = 578, 350
img = cv2.imread('image29.jpg')
img_resize = cv2.resize(img,(width,height))
cv2.imwrite('image29resize.jpg',img_resize)