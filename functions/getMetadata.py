import tkinter as tk, pyperclip, ntpath, sys
from tkinter import filedialog

sys.path.append('../helpers')
from helpers.extractMetadata import extractMetadata
from helpers.selectFileFolder import selectFileFolder
from helpers.message import error, success, yellow

def getMetadata():
    file = selectFileFolder('File')
    name = ntpath.basename(file)
    if len(name) > 40: name = name[:40] + "..."
    metadata = extractMetadata(file)
    if metadata == 'Cant get metadata':
        error('Cant get metadata. ID=getMetadata 1')
    elif metadata:
        pyperclip.copy(metadata)
        # shown_metadata = metadata[:40]
        # if len(metadata) > 40: shown_metadata += "..."
        success('Your metadata is in the clipboard!\n')
        yellow("File: "+ name + "\n\nMetadata: " + metadata)
    else:
        error('This format is not supported. ID=getMetadata 2')