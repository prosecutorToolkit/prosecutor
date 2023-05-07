import sys

sys.path.append('./helpers')
from helpers.yesNo import yesNo
from helpers.message import yellow

def setRegEx():
    while True:
        yellow('Set the Regular expression')
        option = str(input('\n > '))
        yesNo(f'Setted: {option}\nConfirm? (y/n)\n > ')
        if yesNo:
            return option