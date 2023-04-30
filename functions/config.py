import sys

sys.path.append('../helpers')
from helpers.setApiKey import setApiKey
from helpers.banner import banner
from helpers.message import blue, error
from helpers.saveAutoStart import saveAutoStart


maxFuncValue = 12   # update if new functionalities were createdyh
def mainMenuFunctions(): return '''
        \n1. Deep folder scan 🔎
        \n2. Get text of file Ⓐ
        \n3. Get text of screen 🖥
        \n4. Get hash of file/folder #
        \n5. Get metadata of file ␐
        \n6. Compress file/folder 🗜
        \n7. Get IP/URL data 💻
        \n8. Search malware in IP/URL 🦠
        \n9. Search malware in file 🦠
        \n10. Search executables in file 🦠
        \n11. Process and map impacts of phones in cells 📱
        \n12. Download forensically a YouTube Video ▷
        '''

def config():
    while True:
        try:
            blue('\nCONFIGURATION:')
            configOption = int(input('''1. Set startup functionality
                \n2. Set API password of Virus Total
                \n3. Show banner
                \n4. Back
                \n > '''))
                # \n1. Set hash type            [OPTION UNDER DEVELOPMENT]
                # \n3. Set speech of OCR recognition  [OPTION UNDER DEVELOPMENT]
                # \n4. Change program speech    [OPTION UNDER DEVELOPMENT]
        except:
            error('Invalid option, must be a number')
            continue

        if configOption < 0 or configOption > 5:
            # uno menos y uno mas que las opciones posibles
            error('Invalid option, must be between 1 and 5')
            continue

        if configOption == 1:
            while True:
                try:
                    blue('\nSelect the functionality that you want to launch automaticly when you start Prosecutor Toolkit:')
                    # 0 = borrar
                    option = int(input('0. DELETE AUTOLAUNCH {} \n> '.format(mainMenuFunctions())))
                except:
                    error('must set a number')
                    continue
                if option < 0 or option > maxFuncValue:
                    error('must set a valid number')
                    continue
                saveAutoStart('auto_start=', option)
                break
        elif configOption == 2:
            setApiKey()
            break
        elif configOption == 3:
            print('launch banner')
            banner()
            break

        # if configOption == 1:
        #     while True:
        #         try:
        #             option = int(input('''
        #                 HASH TYPE
        #                 \n- 1. SHA-256 
        #                 \n- 2. MD5
        #                 \n > '''))
        #         except:
        #             error('must set 1 or 2')
        #             continue
        #         if int(option) == 1:
        #             # CODE
        #             print('SHA-256 algoritm is setted!')
        #             break
        #         elif int(option) == 2:
        #             # CODE
        #             print('MD5 algoritm is setted!')
        #             break
        #         error('must set 1 or 2')
        # elif configOption == 3:
        #     while True:
        #         try:
        #             option = int(input('''
        #                 OCR RECOGNITION SPEECH:
        #                 \n- 1. English
        #                 \n- 2. Spanish
        #                 \n > '''))
        #         except:
        #             error('must set 1 or 2')
        #         if int(option) == 1:
        #             # CODE
        #             print('English is setted!')
        #         elif int(option) == 2:
        #             # CODE
        #             print('Spanish is setted!')
        #         else:
        #             error('must set 1 or 2')
        # elif configOption == 4:
        #     while True:
        #         option = input('''
        #         OCR RECOGNITION SPEECH:
        #         \n  - 1. English
        #         \n  - 2. Spanish
        #         \n > ''')
        #         try:
        #             if int(option) == 1:
        #                 # CODE
        #                 print('English is setted!')
        #             if int(option) == 2:
        #                 # CODE
        #                 print('Español fue definido!')
        #             break
        #         except:
        #             error('must set 1 or 2')