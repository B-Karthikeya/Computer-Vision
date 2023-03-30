#CONTOUR DETECTION TECHNIQUES

import cv2
import numpy as np

img = cv2.imread("kk.jpg")
img = cv2.resize(img,(1080,720))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(255,0,0),3)
print("no of countours = " ,str(contours))
cv2.imshow("countours",img)
cv2.imshow("thresh" ,thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


