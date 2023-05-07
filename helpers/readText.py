import os
from readTXT import readTXT
from readDocDocx import readDocDocx
from readPDF import readPDF
from readImage import readImage
from message import error

def readText(file):
    text = ''
    
    try:
        ext = os.path.splitext(file)[1]
        if ext == ".txt": text = readTXT(file)
        elif ext == ".doc" or ext == '.docx' or ext == '.odt':
            text = readDocDocx(file)
        elif ext == ".pdf": text = readPDF(file)
        else: text = readImage(file)
    except: error("Cant read: " + str(file))
    
    return text