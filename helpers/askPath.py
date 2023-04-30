from tkinter import filedialog
import tkinter as tk, sys

sys.path.append('../helpers')
from helpers.message import error

def askPath():
    while True:
        root = tk.Tk()
        root.withdraw()
        directory=filedialog.askdirectory()
        if directory == '': error('You havent selected a folder. Try again.')
        else: break

    return directory