import cv2
import math
import argparse

def highlightFace(net,frame,conf_threshold=0.7) :
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn,1,(300,300),[140,117,123],True,False)

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]) :
        confidence = detections[0,0,i,2]
        if confidence > conf_threshold :
            x1 = int(detections[0,0,i,3]*frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameWidth)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameWidth)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn,(x1,y1),(x2,y2),(0,255,0),int(round(frameHeight/150)))

    return  frameOpencvDnn,faceBoxes

parser = argparse.ArgumentParser()
parser.add_argument('--image')
args = parser.parse_args()

face_proto = 'opencv_face_detector.pbtxt'
face_model = 'opencv_face_detector_uint8.pb'
age_model = 'age_net.caffemodel'
age_proto = 'age_deploy.prototxt'
gender_proto = 'gender_deploy.prototxt'
genderModel = 'gender_net.caffemodel'

MODELMEAN_VALUES = (78.4263377603,87.7689143744,114.895847746)
age_list = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)']
gender_list = ['Male','Female']

faceNet = cv2.dnn.readNet(face_model,face_proto)
ageNet = cv2.dnn.readNet(age_model,age_proto)
genderNet = cv2.dnn.readNet(genderModel,gender_proto)

video = cv2.VideoCapture(0)
padding = 20
while cv2.waitKey(1) < 0 :
    hasFrame,frame = video.read()
    if not hasFrame :
        cv2.waitKey()
        break

    resultImg,faceBoxes = highlightFace(faceNet,frame)
    if not faceBoxes :
        print('no faces detected')

    for facebox in faceBoxes  :
        face = frame[max(0,facebox[1]-padding):min(facebox[3]+padding,frame.shape[0]-1),max(0,facebox[0]-padding):min(facebox[2]+padding,frame.shape[1]-1)]
        blob = cv2.dnn.blobFromImage(face,1.0,(277,277),MODELMEAN_VALUES,swapRB = False)
        genderPreds = genderNet.forward()
        gender = gender_list[genderPreds[0].argmax()]
        print(f'Gender ; {gender}')

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = age_list[agePreds[0].argmax()]
        print(f'Age : {age[1:-1]} years')
        cv2.putText(resultImg,f'{gender},{age}',(facebox[0],facebox[1]),1,(0,0,255),5)
        cv2.imshow('detcting age and gender',resultImg)