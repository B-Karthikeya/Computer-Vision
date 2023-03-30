# HISTOGRAM EQUALIZATION USING OPENCV

import cv2
import numpy as np

img = cv2.imread("kk.jpg",0)
img = cv2.resize(img,(1080,720))

equ = cv2.equalizeHist(img,img)
cv2.imshow('original image',img)
cv2.imshow('equalized image',equ)

image = np.hstack((img,equ))
cv2.imshow('merged image',img)

clahe = cv2.createCLAHE(clipLimit=5)
final_image = clahe.apply(img)
cv2.imshow('final image',final_image)
cv2.imwrite('histogram_equalized_image.jpg',final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()