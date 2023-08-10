import sys

sys.path.append('../helpers')
from helpers.setApiKey import setApiKey

def readConfig(value):
    try:
        with open("conf.py", 'r') as file:
            content = file.read()
            lines = content.split('\n')
            for line in lines:
                if line.startswith(value):
                    _, valor = line.split('=')
                    returnValue = valor.strip().strip("'")
    except:
        returnValue = ''
    return returnValue