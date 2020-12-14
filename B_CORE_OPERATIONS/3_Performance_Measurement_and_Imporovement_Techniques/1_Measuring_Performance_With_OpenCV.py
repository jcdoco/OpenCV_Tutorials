import cv2
import numpy as np

img = cv2.imread('fusion.jpg')

#return the number of clock-cycles after a reference event
#launch this function befaore the code (times 1)
e1 = cv2.getTickCount()


#Image blurring(Blur)is achieved by convolving the image with a low-pass filter kernel.

for i in xrange(5,49,2):
#the function cv2.medianBlur() computes the median of all the pixels under the kernel window 
#and the central pixel is replaced with this median value   
    img = cv2.medianBlur(img,i)


#repeat this function after the code (times 2)
e2 = cv2.getTickCount()

#cv2.getTickFrequency function returns the frequency of clock-cycles, 
# or the number of clock-cycles per second
t = (e2 - e1)/cv2.getTickFrequency()
print t

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows





