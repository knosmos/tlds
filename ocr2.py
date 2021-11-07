import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

garbage = ["\n","\x0c","="," "]

# load image
def run(filename):
    image = cv2.imread(filename)
    cv2.imshow("image",image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",image)
    (thresh, image) = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh",image)
    res = pytesseract.image_to_string(image, config = "0123456789+-=")
    for i in garbage:
        res = res.replace(i,"")
    print(res+"="+str(eval(res)))
    return res+"="+str(eval(res))

if __name__ == "__main__":
    run("temp.jpg")
    cv2.waitKey(0)