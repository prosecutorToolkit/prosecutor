import tkinter as tk, zipfile, os, sys, ntpath
from tkinter import filedialog

sys.path.append('../helpers')
from helpers.timeReport import timeReport
from helpers.message import success, error, blue, yellow
from helpers.yesNo import yesNo
from helpers.launchFile import launchFile

def compressFile():
    root = tk.Tk()
    root.withdraw()

    while True:
        try:
            blue('What do you want to compress?\n 1. File/s\n 2. Folder')
            option = int(input(' > '))
            if option < 1 or option > 2:
                error('You must select 1 or 2')
                pass
            else:
                if option == 1:
                    filesFolders = filedialog.askopenfilenames(parent=root, title="Select file/s", multiple=True)
                elif option == 2:
                    filesFolders = filedialog.askdirectory(parent=root, title="Select folder/s")
                if not len(filesFolders):
                    error('No file was selected')
                    pass
                break
        except:
            error('You must select 1 or 2')
            pass

    if type(filesFolders) == str:
        yellow('Selected folder:\n > ' + filesFolders)
    else:
        yellow('Selected items:')
        for item in filesFolders:
            yellow(' > ' + str(ntpath.basename(item)))

    directory=filedialog.askdirectory(title='Choose the folder where save the Zip file')
    if directory != "": os.chdir(directory)
    destination_path = os.getcwd()
    if not len(destination_path):
        error('No folder was selected')
    else:
        folder_zip = destination_path + '/Prosecutor - ' + timeReport() + '.zip'
        with zipfile.ZipFile(folder_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if option == 1:
                for value in filesFolders:
                    try:
                        zipf.write(value, os.path.basename(value))
                    except:
                        error(f'Cant compress in Zip the file {value}\n')
            else:
                for actualFolder, subFolder, files in os.walk(filesFolders):
                    for archivo in files:
                        route = os.path.join(actualFolder, archivo)
                        relativeRoute = os.path.relpath(route, filesFolders)
                        zipf.write(route, relativeRoute)
        success('Done!')

        confirm = yesNo('\nDo you want to launch the Zip file? (y/n)\n > ')
        if confirm: launchFile(folder_zip)