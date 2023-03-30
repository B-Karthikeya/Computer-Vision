import cv2
import numpy as np

img = cv2.imread('kk.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(1080,760))
ret,thresh = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh2 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
ret,thresh3 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,thresh4 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original',img)
cv2.imshow('thresh binary',thresh)
cv2.imshow('thresh binary inverse',thresh1)
cv2.imshow('thresh trunc',thresh2)
cv2.imshow('thresh to zero',thresh3)
cv2.imshow('thresh to zero inverse',thresh4)
cv2.waitKey(0)
