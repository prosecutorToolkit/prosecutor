import sys, ntpath, pyperclip

sys.path.append('./helpers')
from helpers.message import error, yellow, success
from helpers.selectFileFolder import selectFileFolder
from helpers.readText import readText

def getText():
    file = selectFileFolder('File')
    name = ntpath.basename(file)
    if len(name) > 40:
        name = name[:40] + "..."
    print('Selected file: ' + name)

    text = readText(file)

    if not text:
        error("Prosecutor can't read this file")

    else: 
        pyperclip.copy(text)
        show_text = text[:40]
        if len(text) > 40: show_text += "...continue..."
        success("\nYour text is in the clipboard!")
        yellow("\nFile: " + name + "\n\nText: " + show_text)
            