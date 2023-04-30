## AGREGAR OTROS FORMATOS EJECUTABLES Y GENERAR LA COMBINACION DE MAYS Y MINS CON INDIFFERENT

import sys, os, ntpath, platform

from scanFileInVT import scanFileInVT

sys.path.append('../helpers')
from helpers.launchFile import launchFile
from helpers.yesNo import yesNo
from helpers.selectFileFolder import selectFileFolder
from helpers.message import yellow, green, red
from helpers.yesNo import yesNo

def scanFileInHEX():
    file = selectFileFolder('File')

    with open(file,'rb') as f:
        buff = f.read()
    out_hex = ['{:02X}'.format(b) for b in buff]

    x = ""

    for value in out_hex: x+=" " + value

    a_string = bytes.fromhex(x)

    if platform.system() == "Windows":
        a_string = a_string.decode("ansi", errors='ignore')
    else:
        a_string = a_string.decode("ascii", errors='ignore')

    # agregar otros ejecutables como "sh"
    exe = ["exe", "Exe", "eXe", "exE", "EXe", "ExE", "eXE", "EXE"]

    match = False

    for e in exe:
        if e in a_string: match = True

    if match: red("\nPOSITIVE! The file probably is a executable file!")
    else: green("\nNEGATIVE: We cant find executable files.")

    confirm = yesNo("\nDo you want the hexadecimal code? (y/n)\n  > ")

    if confirm:
        yellow("\nSelect where you want to save it")
        folder = selectFileFolder()
        name = ntpath.basename(file)
        filePath = os.path.join(folder, 'Prosecutor - Hex data of ' + name + '.txt')
        with open(filePath, 'wt') as file: file.write(a_string)
        confirm = yesNo('Do you want to launch the file? (y/n)\n > ')
        if confirm: launchFile(filePath)

    confirm = yesNo("\n\nWe also recommend scan it with Virus Total, do you want to launch this tool? (y/n)\n  > ")
    if confirm: scanFileInVT(file)