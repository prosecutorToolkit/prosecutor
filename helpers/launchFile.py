import os, subprocess, platform, sys

sys.path.append('../helpers')
from message import error


def launchFile(filePath):
    try:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filePath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filePath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filePath))
    except:
        error('Cant launch the file')
