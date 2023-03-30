# IMAGE MASKING

import cv2
import numpy as np

img = cv2.imread("kk.jpg")
img = cv2.resize(img,(1080,760))
cv2.imshow("original",img)

mask = np.zeros(img.shape[:2],dtype='uint8')
# cv2.rectangle(mask,(100,100),(980,660),255,-1)
cv2.circle(mask,(500,350),300,255,-1)

masked_image = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow("masked image",masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()