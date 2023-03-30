#smoothing techniques for images


import cv2
import numpy as np

img = cv2.imread("parrot.jpg")
cv2.imshow("parrot image",img)
blur = cv2.blur(img,(5,5))

gauss = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)
box = cv2.boxFilter(img,0,(7,7))

cv2.imshow(' blur ',blur)
cv2.imshow('gaussian blur ',gauss)
cv2.imshow("median blur ",median)
cv2.imshow("bilateral filter ",bilateral)
cv2.imshow("box filter ",box)



