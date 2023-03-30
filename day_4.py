#edge detection
import cv2
import numpy as np

# img = cv2.imread("parrot.jpg")
img = cv2.imread("kk.jpg")
img= cv2.resize(img,(1050,1060))
cv2.imshow("parrot image",img)

#sobel edge detector
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(img,(5,5))
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
laplacian = cv2.Laplacian(gray,cv2.CV_64F)

cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('laplacian',laplacian)
# cv2.waitKey(0)

#cany edge detector

gauss_blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(gauss_blur,100,200)
cv2.imshow("canny edges",canny)
cv2.waitKey(0)
