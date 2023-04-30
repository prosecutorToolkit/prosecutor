import tkinter as tk, colorama, zipfile, os, sys
from tkinter import filedialog

sys.path.append('../helpers')
from helpers.timeReport import timeReport
from helpers.message import success, error
from helpers.selectFileFolder import selectFileFolder


def compressFile():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(parent=root, title="Select files", multiple=True)

    if len(files) == 0:
        error('No file was selected')
    else:
        directory=filedialog.askdirectory(title='Choose the folder where save the outout file')
        if directory != "": os.chdir(directory)
        destination_path = os.getcwd()
        if len(destination_path) == 0:
            error('No folder was selected')
        else:
            folder_zip = destination_path + '/Prosecutor - ' + timeReport() + '.zip'
            zipF = zipfile.ZipFile(folder_zip, 'w')
            for value in files:
                zipF.write(os.path.basename(value), compress_type=zipfile.ZIP_DEFLATED)
            zipF.close()
            success('Done!')