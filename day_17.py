# DETECTION OF MULTIPLE SHAPES USING EDGE DETECTOR
import cv2
import numpy as np

img = cv2.imread('shapes.png')
# img = cv2.imread('kk.jpg')
# img = cv2.resize(img,(1080,720))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image',gray)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

i=0
for contour in contours :
    if i==0 :
        i=1
        continue
    approx = cv2.approxPolyDP(contour,0.04*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[contour],-1,(0,0,0),4)

    # find the center of the image
    M = cv2.moments(contour)
    if M['m00']!=0.0 :
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    # shape
    if len(approx) == 3 :
        cv2.putText(img,'Triangle',(x,y),0,0.6,(0,0,0),2)
    elif len(approx) == 4 :
        cv2.putText(img,'Quadrilateral',(x,y),0,0.6,(0,0,0),2)
    elif len(approx) == 5 :
        cv2.putText(img,'Polygon',(x,y),0,0.6,(0,0,0),2)
    elif len(approx) == 6 :
        cv2.putText(img,'Hexagon',(x,y),0,0.6,(0,0,0),2)
    else :
        cv2.putText(img,'Circle',(x,y),0,0.6,(0,0,0),2)

cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


