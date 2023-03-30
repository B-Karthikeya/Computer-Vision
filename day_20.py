# BACKGROUND SUBTRACTION BY OPEN CV

import cv2
import numpy as np

cap = cv2.VideoCapture('stock.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1 :
    res,img = cap.read()
    fgmask = fgbg.apply(img)

    cv2.imshow('original',img)
    cv2.imshow('fgmask',fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k == 27 :
        break

cap.release()
cv2.destroyAllWindows()