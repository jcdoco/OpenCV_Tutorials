import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bambou.jpeg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
abs_sobel64f = np.absolute(sobelx)
sobel_8u = np.uint8(abs_sobel64f)
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)


plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(abs_sobel64f,cmap = 'gray')
plt.title('abs_sobel64F'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel_8u'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobelx8u'), plt.xticks([]), plt.yticks([])


plt.show()
