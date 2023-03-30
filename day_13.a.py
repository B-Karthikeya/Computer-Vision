# OPTICAL CHARACTER RECOGNITION
# IMAGE TO TEXT

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
# img = cv2.imread("quote1.png")
img = cv2.imread("number_plate1.jpg")
text = pytesseract.image_to_string(img)
print(text)
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()