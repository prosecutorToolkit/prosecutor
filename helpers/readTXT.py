def readTXT(file):
    try:
        err = False
        text = ""
        with open(file) as f:
            text_5 = f.readlines()
        f.close()
        for line in text_5:
            text += line
        text = text.replace("\n", " ")
    except: text = 'ERROR'
    return text