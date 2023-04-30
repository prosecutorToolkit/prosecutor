import textract

def readDocDocx(file):
    try:
        text = str(textract.process(file))
        text = text[2:-1]
        text = text.replace("\n", " ")
    except:
        text = 'ERROR'
    return text