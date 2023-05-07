#!/usr/bin/env python3

# Name: Prosecutor Toolkit
# Version: 1.0
# Date and place of creation: 18/06/2022, La Plata - Argentina
# Publish: 23/03/2023, La Plata - Buenos Aires - Argentina
# Author: Tobias Rimoli
# Contact: tobiasrimoli@protonmail.com

import os, os.path, sys
from pathlib import Path
from tkinter import *
from turtle import *

sys.path.append('./functions')
from functions.scanScreen import scanScreen
from functions.deepScanFolder import deepScanFolder
from functions.createReportsFromDB import createReportsFromDB
from functions.getMetadata import getMetadata
from functions.getIPData import getIPData
from functions.getText import getText
from functions.getHash import getHash
from functions.compressFile import compressFile
from functions.scanIPURLInVT import scanIPURLInVT
from functions.scanFileInVT import scanFileInVT
from functions.scanFileInHEX import scanFileInHEX
from functions.mapCreatorForPhoneCellsData import __init__ as mapCreatorForPhoneCellsData
from functions.config import config, mainMenuFunctions
from functions.about import about
from functions.getYoutubeVideo import getYoutubeVideo

sys.path.append('./helpers')
from helpers.banner import banner
from helpers.message import blue, error

mainMenuOthers = '''
        \nc. Configuration
        \na. About
        \ne. Exit
        \n > '''

def launchFunctions(option):
    if option == 1: deepScanFolder()
    elif option == 2: createReportsFromDB()
    elif option == 3: getText()
    elif option == 4: scanScreen()
    elif option == 5: getHash()
    elif option == 6: getMetadata()
    elif option == 7: compressFile()
    elif option == 8: getIPData()
    elif option == 9: scanIPURLInVT()
    elif option == 10: scanFileInVT()
    elif option == 11: scanFileInHEX()
    elif option == 12: mapCreatorForPhoneCellsData()
    elif option == 13: getYoutubeVideo()
    elif option == 'c' or option == 'C': config()
    elif option == 'a' or option == 'A': about()

class Prosecutor:
    def __init__(self):
        super().__init__()
        firstTime = True
        passF = False
        while True:
            if firstTime:
                with open("conf.py", 'r') as file:
                    content = file.read()
                    lines = content.split('\n')
                    for line in lines:
                        if line.startswith('auto_start'):
                            _, valor = line.split('=')
                            option = valor.strip().strip("'")
                            print("PRESELECTED FUNCTIONALITY: " + str(int(option))) # check
                            launchFunctions(int(option))
                            passF = True
                            break
                        else: option = ""
                if passF: continue
                banner()
                blue('Press [enter] to launch the menu')
                option = input(' > ')
                # try: 
                blue("What do you want to do?")
                option = input(mainMenuFunctions() + mainMenuOthers)
                if option == 'e' or option == 'E': break
                elif option != 'c' and option != 'C' and option != 'a' and option != 'A':
                    option = int(option)
                launchFunctions(option)
                # except: error('Invalid option. ID=A1')
            else:
                blue('Press [enter] to menu')
                option = input(' > ')
                # try:
                blue("What do you want to do?")
                option = input(mainMenuFunctions() + mainMenuOthers)
                if option == 'e' or option == 'E': break
                elif option != 'c' and option != 'C' and option != 'a' and option != 'A':
                    option = int(option)
                launchFunctions(option)
                # except: error('Invalid option. ID=A2')
            firstTime = False
        quit()


if __name__ == "__main__":
    prosecutorObj = Prosecutor()