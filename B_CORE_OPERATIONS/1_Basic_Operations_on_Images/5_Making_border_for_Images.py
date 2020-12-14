import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fusion.jpg')
color = [0,0,255]
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

reflect = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_REFLECT,value=color)
reflect101 = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_REFLECT101,value=color)
constant = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_CONSTANT,value=color)
wrap = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_WRAP,value=color)
replicate = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_REPLICATE,value=color)


plt.subplot(231),plt.imshow(constant),plt.title('Constant')
plt.subplot(232),plt.imshow(reflect),plt.title('Reflect')
plt.subplot(233),plt.imshow(reflect101),plt.title('Reflect101')
plt.subplot(234),plt.imshow(wrap),plt.title('Wrap')
plt.subplot(235),plt.imshow(replicate),plt.title('Replicate')

plt.show()