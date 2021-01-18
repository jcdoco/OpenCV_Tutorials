import cv2
import numpy as np

img = cv2.imread('joker.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist,bins = np.histogram(img.ravel(),256,[0,256])
print(hist)