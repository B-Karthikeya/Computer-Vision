import cv2
import numpy as np

img = cv2.imread("kk.jpg")
img= cv2.resize(img,(1050,1060))
cv2.imshow("parrot image",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("parrot image gray",gray)
cv2.imshow("parrot image hsv",hsv)

r,g,b = cv2.split(img)
cv2.imshow("parrot image red",r)
cv2.imshow("parrot image blue",b)
cv2.imshow("parrot image green",g)
cv2.waitKey(0)

