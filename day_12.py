# PLAYING VIDEO IN REVERSE MODE

import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# while 1 :
#     res,vid = cap.read()
#     cv2.imshow("frame",vid)
#     if cv2.waitKey(25) & 0xFF == ord("q") :
#         break
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('WhatsApp.mp4')
res,vid = cap.read()
count = 0
frame_list = []
while res  :

    res,vid = cap.read()
    frame_list.append(vid)
    count+=1

frame_list.pop()

for frame in frame_list:
    cv2.imshow("frame",frame)

    if cv2.waitKey(25) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()

frame_list.reverse()

for frame in frame_list :
    cv2.imshow("reverse video",frame)
    if cv2.waitKey(25) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()

