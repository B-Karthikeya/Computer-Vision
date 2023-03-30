# TEMPLATE MATCHING IN OPEN CV

import cv2
import numpy as np

image = cv2.imread("coca_cola_1.jpg")
# image = cv2.resize(image,(1080,720))
template = cv2.imread("Coca-Cola_logo.png")

img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
temp_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(img_gray,temp_gray,cv2.TM_CCOEFF_NORMED)
(minval,maxval,minloc,maxloc) = cv2.minMaxLoc(result)

startX,startY = maxloc
endX = startX + template.shape[0]
endY = startY + template.shape[1]

cv2.rectangle(image,(startX,startY),(endX,endY),(255,0,0),3)

cv2.imshow('original',image)
# cv2.imshow('gray image',img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()