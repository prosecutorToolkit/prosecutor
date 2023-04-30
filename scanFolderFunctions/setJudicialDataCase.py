import sys

sys.path.append('./helpers')
from helpers.message import yellow
from helpers.yesNo import yesNo


def setJudicialDataCase():
    while True:
        yellow('\nSet the data of the judicial case (case number, cover sheet, judge, prosecutor): ')
        data = '\nCase number: ' + input('\nCase number > ')
        data += '\nCover sheet: ' + input('\nCover sheet > ')
        data += '\nJudge: ' + input('\nJudge > ')
        data += '\nProsecutor: ' + input('\nProsecutor > ')
        confirm = yesNo('DATA SETTED:\n{}\n\nConfirm? (y/n)\n > '.format(data))
        if confirm: break
        else: print('\nOk. Try again.')
    return data.replace('\n', '  ')
