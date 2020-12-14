import cv2

img1 = cv2.imread('effect_image.jpg')
img2 = cv2.imread('effect_image2.jpg')

addW = img1 + img2
subsW = img1 - img2
cv2.imwrite('effect_imageA.jpg',subsW)
cv2.imwrite('effect_imageB.jpg',addW)
#print(addW)
#print(subsW)

add1W = cv2.add(img1, img2)
subs1W = cv2.subtract(img2,img2)
subs2W = cv2.subtract(img1,img2)
cv2.imwrite('add1W.jpg',add1W)
cv2.imwrite('subs1W.jpg',subs1W)
cv2.imwrite('subs2W.jpg',subs2W)


cv2.imshow("add", addW)
cv2.imshow("subs", subsW)
cv2.imshow("add1", add1W)
cv2.imshow("subs1", subs1W)
cv2.imshow("subs2", subs2W)

cv2.waitKey(0)
cv2.destroyAllWindows






