#MORPHOLOGY TECHNIQUES

import cv2
import numpy as np

#img = cv2.imread('k.png')
img = cv2.imread('kk.jpg')
img = cv2.resize(img,(1080,760))
kernal = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernal)
erosion = cv2.erode(img,kernal)
open_morph = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
close_morph = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
morph_grad = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)

cv2.imshow('dialtion',dilation)
cv2.imshow('erosion',erosion)
cv2.imshow('k letter',img)
cv2.imshow('open morphology',open_morph)
cv2.imshow('close morphology',close_morph)
cv2.imshow('gradient morphology',morph_grad)
cv2.waitKey(0)
