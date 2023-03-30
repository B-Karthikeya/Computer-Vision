import cv2
import numpy as np

image = cv2.imread("Lamborghini.jpg")
image = cv2.resize(image,(1868,930))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# applying SIFT detector
sift = cv2.SIFT_create()
keypoint,descriptors = sift.detectAndCompute(image,None)

# marking the keypoint on the image using circles

img = cv2.drawKeypoints(gray,keypoint,image,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

