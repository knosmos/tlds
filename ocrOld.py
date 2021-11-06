import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# load image
image = cv2.imread('worksheet.jpg')

num_columns = 2
column_width = image.shape[1] // num_columns
columns = []
for i in range(num_columns):
    columns.append(image[:, i*column_width:(i+1)*column_width])
for column in columns:
    print(pytesseract.image_to_string(column, config = "0123456789+-="))