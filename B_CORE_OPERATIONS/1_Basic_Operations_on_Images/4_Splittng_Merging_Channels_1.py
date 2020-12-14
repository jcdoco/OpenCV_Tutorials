import cv2
import numpy as np

img = cv2.imread('joker.jpeg')


b,g,r = cv2.split(img)

zeros = np.zeros(img.shape[:2],dtype='uint8')
print(zeros.shape)

cv2.imshow("blue channel",cv2.merge([b,zeros,zeros]))

cv2.imshow("green channel",cv2.merge([zeros,g,zeros]))

cv2.imshow("red channel",cv2.merge([zeros,zeros,r]))

cv2.imshow("RGB",cv2.merge([r,g,b]))
cv2.imshow("BGR",cv2.merge([b,g,r]))

cv2.imshow("sample1",cv2.merge([b+100,zeros,g]))
cv2.imshow("sample2",cv2.merge([zeros,r+100,zeros]))
cv2.imshow("sample3",cv2.merge([zeros,r,g+100]))

cv2.waitKey(0)
cv2.destroyAllWindows()
