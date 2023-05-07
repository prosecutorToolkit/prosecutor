import re

def searchWithRegEx(regex, text):
    matchList = re.findall(regex, text)
    extML = len(matchList)
    matchF = ''

    if extML >1:
        for idL, value in enumerate(matchList):
            if idL +1 == extML:
                matchF += value
            matchF += f'{str(idL)}) ' + value
    else:
        try:
            matchF = str(matchList[0])
        except:
            matchF = ''
    
    return matchF