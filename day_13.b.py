# OPTICAL CHARACTER RECOGNITION
#TEXT TO AUDIO

import cv2
import pytesseract
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("quote1.png")
text = pytesseract.image_to_string(img)
print(text)

language = 'en'
audio = gTTS(text=text,lang=language,slow= False)
audio.save('audio.mp3')
os.system('audio.mp3')
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()