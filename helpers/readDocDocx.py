import textract, os
from getTextFromDocument import getTextFromDocument

def readDocDocx(file):
    try:
        text = str(textract.process(file))
        text = text[2:-1]
        ext = os.path.splitext(file)[1].lower()
        if ext == '.docx' or ext == '.odt':
            text += getTextFromDocument(file)
        text = text.replace("\n", " ")
    except:
        text = 'Cant read file ID=RDD'
    return text