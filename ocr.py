import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class ReadText:

    def __init__(self, fileName, columns):
        self.image = cv2.imread(fileName)
        self.num_columns = columns
        self.column_width = self.image.shape[1] // self.num_columns

        self.columns = []

        for i in range(self.num_columns):
            self.columns.append(self.image[:, i*self.column_width:(i+1)*self.column_width])

    def blackWhite(self, originalImage):
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        
        return blackAndWhiteImage

    def saveImage (self, valueList):

        for i in range(len(valueList)):
            cv2.imwrite("/Users/nick/Documents/Python/Text Summary/image"+str(i)+".jpg", valueList[i])

    def createBW ( self ):

        self.columnsBW = []

        for i in range(self.num_columns):
            
            self.columnsBW.append(ReadText.blackWhite(self, self.columns[i]))

        ReadText.saveImage(self, self.columnsBW)

    def toString(self, valueList):

        self.text = []

        for i in range(len(valueList)):
            self.text.append (pytesseract.image_to_string(valueList[i]).replace('\x0c', ''))

class EvaluateString:

    def __init__ (self, textList):
        self.zones = len(textList)
        self.text = textList

    def splitEquation (self):

        self.equations = []
        sectionText = ""

        for i in range(self.zones):
            sectionText += self.text[i]
            sectionText = sectionText.replace(' ', '')

        self.equations = sectionText.split("\n")

        self.equations.pop()
        
        for value in self.equations:

            if value == '':
                self.equations.remove(value)
                continue

            if '=' not in value:
                self.equations.remove(value)

        

    def solveEquation (self):

        self.answers = []

        for equation in self.equations:

            if '=' in equation:
                equation = equation.replace('=', '')

            else:
                continue
    
            self.answers.append(eval(equation))


def run(filename):
    addition = ReadText(filename, 1) # Divide text into columns
    addition.createBW() # Convert to B&W
    addition.toString(addition.columnsBW) #Convert B&W to Text

    addString = EvaluateString(addition.text)
    addString.splitEquation()
    print(addString.equations)
    addString.solveEquation()

    print(addString.answers)

    return addString.equations[0]+str(addString.answers[0])