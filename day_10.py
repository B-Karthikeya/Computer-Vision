# OTSU THRESHOLDING

import cv2
import numpy as np

img = cv2.imread("parrot.jpg")
# img = cv2.resize(img,(1080,720))
cv2.imshow("original",img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,120,225,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("threshold image",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()