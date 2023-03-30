# IMAGE MASKING

import cv2
import numpy as np

rectangle = np.zeros((300,300),dtype = 'uint8')
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("rectangle",rectangle)

circle = np.zeros((300,300),dtype = 'uint8')
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("circle",circle)

bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow("and",bitwise_and)

bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow("bitwise or",bitwise_or)

bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("bitwise xor",bitwise_xor)

bitwise_not_rec = cv2.bitwise_not(rectangle)
cv2.imshow("bitwise not rectangle",bitwise_not_rec)

bitwise_not_cir = cv2.bitwise_not(circle)
cv2.imshow("bitwise not circle",bitwise_not_cir)


cv2.waitKey(0)
cv2.destroyAllWindows()