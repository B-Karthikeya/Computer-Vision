# REAL TIME MULTI COLOR DETECTION IN OPENCV

import cv2
import numpy as np

# capturing vedio through webcam
cap = cv2.VideoCapture(0)

while 1:
    _,img = cap.read()
    # converting frame to hsv
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # red color
    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)

    # blue color
    blue_lower = np.array([99,80,2], np.uint8)
    blue_upper = np.array([120,255,255], np.uint8)

    # yellow color
    yellow_lower = np.array([22,180,200], np.uint8)
    yellow_upper = np.array([60,255,255], np.uint8)

    # white color
    white_lower = np.array([0,0,200], np.uint8)
    white_upper = np.array([180,255,30], np.uint8)

    # green color
    green_lower = np.array([25,52,72], np.uint8)
    green_upper = np.array([102,255,255], np.uint8)

    # black color
    black_lower = np.array([0,0,0], np.uint8)
    black_upper = np.array([180, 255, 30], np.uint8)

    # all color together
    red =cv2.inRange(hsv,red_lower,red_upper)
    blue = cv2.inRange(hsv,blue_lower,blue_upper)
    yellow = cv2.inRange(hsv,yellow_lower,yellow_upper)
    white = cv2.inRange(hsv,white_lower,white_upper)
    black = cv2.inRange(hsv,black_lower,black_upper)
    green = cv2.inRange(hsv,green_lower,green_upper)

    # morphological transformation - dilation
    kernal = np.ones((5,5),"uint8")

    red = cv2.dilate(red,kernal)
    res_red = cv2.bitwise_and(img,img,mask = red)

    blue = cv2.dilate(blue,kernal)
    res_blue = cv2.bitwise_and(img,img,mask =blue)

    yellow = cv2.dilate(yellow,kernal)
    res_yellow = cv2.bitwise_and(img,img,mask = yellow)

    white = cv2.dilate(white,kernal)
    res_white = cv2.bitwise_and(img,img,mask = white)

    black = cv2.dilate(black,kernal)
    res_black = cv2.bitwise_and(img,img,mask = black)

    green = cv2.dilate(green,kernal)
    res_green = cv2.bitwise_and(img,img,mask = green)

    # tracking colors
    contours,heirarchy = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours) :
        area = cv2.contourArea(contour)
        if area>300 :
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.putText(img,'red color',(x,y),0,1,(0,0,255))

    contours, heirarchy = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.putText(img, 'blue color', (x, y), 0, 1, (0, 0, 255))

    contours, heirarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.putText(img, 'yellow color', (x, y), 0, 1, (0, 0, 255))

    contours, heirarchy = cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.putText(img, 'white color', (x, y), 0, 1, (0, 0, 255))

    contours, heirarchy = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.putText(img, 'black color', (x, y), 0, 1, (0, 0, 255))

    contours, heirarchy = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.putText(img, 'green color', (x, y), 0, 1, (0, 0, 255))
    cv2.imshow('clolor tracking', img)
    if cv2.waitKey(10) & 0xFF == ord('q') :
        cap.release()
        cv2.destroyAllWindows()
        break

        