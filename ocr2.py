import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

garbage = [
    "\n",
    "\x0c",
    "=",
    " "
]

# load image
def run(filename):
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, image) = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
    res = pytesseract.image_to_string(image, config = "0123456789+-=")
    for i in garbage:
        res = res.replace(i,"")
    print(res+"="+str(eval(res)))
    return res+"="+str(eval(res))