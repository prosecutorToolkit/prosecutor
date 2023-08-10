import tkinter as tk, sys, os
from tkinter import filedialog

sys.path.append('./helpers')
from helpers.message import title, error
from helpers.yesNo import yesNo

def selectFileFolder(typePath = ''):  # typePath = Target / Destination / DB
    title('SELECT ' + typePath.upper())

    while True:
        root = tk.Tk()
        root.withdraw()
        
        if typePath == 'File' or typePath == 'DB':
            target = filedialog.askopenfilename()
        else:
            target = filedialog.askdirectory()
        if len(target) < 3:    # 3 para admitir escanear unidades enteras como D:\
            error('Invalid target. ID=SFF1')
            continue
        if typePath == 'DB':
            if os.path.splitext(target)[1].lower() != '.db':
                error('The file is not a database. ID=SFF2')
                continue
            break
        else:
            shownTarget = target[-40:]
            if len(target) > 40: shownTarget = "..." + shownTarget
            confirm = yesNo('> {} path: {}\nConfirm? (y/n)\n> '.format(typePath, shownTarget))
            if confirm: break
            else: continue

    return target