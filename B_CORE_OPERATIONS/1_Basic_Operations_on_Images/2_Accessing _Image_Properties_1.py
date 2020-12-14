import cv2
import numpy as np
img = cv2.imread('joker.jpeg')

px = img[100,100]
print px

blue = img[100,100,0]
print blue

img[100,100] = [255,255,255]
print img[100,100]

print img.item(10,10,2)

img.itemset((10,10,2),100)
print img.item(10,10,2)

print img.shape
print img.size
print img.dtype
