import pytesseract
from PIL import Image

def readImage(file):
    text = ''
    try:
        img = Image.open(file)
        img = img.convert('L')  # convert to gray scale
        text = pytesseract.image_to_string(img)
        text = text.replace('\n', ' ').replace('  ', ' ')
    except:
        print("Cant read file. ID=ReadImage")
        pass

    return text