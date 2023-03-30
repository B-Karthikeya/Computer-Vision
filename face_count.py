import cv2
import numpy as np

face_detector1 = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_detector1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

image = cv2.imread('bday.jpg')
image = cv2.resize(image,(1080,720))

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_detector1.detectMultiScale(gray_image)

print(type(faces))

if len(faces) == 0 :
    print('no faces found')

else :
    print(faces)
    print(faces.shape)
    print('no of faces detected = ',faces.shape[0])

    for (x,y,w,h) in faces :
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)

    cv2.rectangle(image,(0,image.shape[0]-25),(270,image.shape[0]),(255,255,255),-1)
    cv2.putText(image,'no of faces detected '+ str(faces.shape[0]),(0,image.shape[0]-10),0,0.5,(0,0,0),1)

    cv2.imshow('image with faces',image)

cv2.waitKey(0)
cv2.destroyAllWindows()