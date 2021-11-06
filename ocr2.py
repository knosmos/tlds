import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# load image
image = cv2.imread('math (2).jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, image) = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh",image)
cv2.waitKey(0)
print(pytesseract.image_to_string(image, config = "0123456789+-="))