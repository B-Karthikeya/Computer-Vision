# MULTIPLE FILTERS USED IN IMAGE PROCESSING
import cv2
import numpy as np

img = cv2.imread('kk.jpg')
img = cv2.resize(img,(1080,720))


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
brightness = cv2.convertScaleAbs(img,beta=60)
kernal = np.array([[-1,-1,-1,],[-1,9.5,-1],[-1,-1,-1]])
sharpness = cv2.filter2D(img,-1,kernal)
sk_gray,sk_color = cv2.pencilSketch(img,sigma_s=60,sigma_r=0.07,shade_factor=0.1)
hdr = cv2.detailEnhance(img,sigma_s=150,sigma_r=0.15)
inv = cv2.bitwise_not(img)

cv2.imshow('gray image',gray)
cv2.imshow('brightness image',brightness)
cv2.imshow('pencil sketch1',sk_gray)
cv2.imshow('pencil_sketch2',sk_color)
cv2.imshow('hdr image',hdr)
# cv2.imwrite('kk_hdr.jpg',hdr)
cv2.imshow('inver filter',inv)


cv2.waitKey(0)
cv2.destroyAllWindows()