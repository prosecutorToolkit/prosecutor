import os, sys

sys.path.append('./helpers')
from helpers.message import error


def setDesktopAsDestFolder():
    try:
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        isdir = os.path.isdir(desktop)
        if isdir == False:
            desktop = os.path.join(os.path.expanduser('~'), 'Escritorio')
            isdir = os.path.isdir(desktop)
            if isdir == False:
                error("Prosecutor can't find desktop, the languaje of your operative system is not supported. Please set the destination folder manually.")
                return False
        else:
            shownDesktop = desktop[-40:]
            if len(desktop) > 40: shownDesktop = "..." + shownDesktop
            print('> Destination path: {}'.format(shownDesktop))
            return desktop
    except: error("Unknown. ID=S1")