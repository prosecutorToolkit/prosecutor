import sys, pyperclip

sys.path.append('../helpers')
from helpers.merkleTree import merkleTree
from helpers.getsha256file import getsha256file
from helpers.message import error, success, yellow, show
from helpers.selectFileFolder import selectFileFolder

def getHash():
    while True:
        try:
            option = int(input('''
                WHAT DO YOU WANT TO HASH?
                \n- 1. A file
                \n- 2. A folder (merkle tree)
                \n > '''))
        except:
            error('Must set 1 or 2')
        if int(option) == 1:
            yellow('Hash a file was selected')
            f_hash_file()
            break
        elif int(option) == 2:
            yellow('Hash a folder was selected')
            directory = selectFileFolder('Target')
            try:
                merkleHash = merkleTree(directory)
                if not merkleHash:
                    error('Its not a valid folder. Try again.')
                    continue
                success("Your hash is in the clipboard!")
                show("Directory selected:", directory)
                show("Hash of directory:", merkleHash)
            except:
                error("Unknown error hashing folder")
            break
        else:
            error('Must set 1 or 2')

def f_hash_file():
    file = selectFileFolder('File')

    hashFile = getsha256file(file)

    if len(file) == 0:
        error("No file was selected")
    if hashFile == "":
        error("Prosecutor can't hash this file")
    else:
        pyperclip.copy(hashFile)
        success('\n\nSuccess! Your hash is in the clipboard!')
        show("\nHash:", hashFile)