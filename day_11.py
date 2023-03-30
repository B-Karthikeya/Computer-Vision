# INSERTING SHAPES AND TEXT TO IMAGES

import cv2
import numpy as np

img = cv2.imread("kk.jpg")
img = cv2.resize(img,(1080,760))
# cv2.imshow("original",img)

cv2.circle(img,(300,250),50,(0,0,0),10)
cv2.rectangle(img,(300,50),(500,300),(255,0,0),8)
cv2.line(img,(600,400),(800,150),15)
# font = cv2.FONT_HERSHEY_SIMPLE
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"BOORLA KARTHIKEYA",(100,600),7,5,(255,255,0),10)
cv2.imshow("IAMGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7'''