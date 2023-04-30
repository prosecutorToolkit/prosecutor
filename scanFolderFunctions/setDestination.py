import sys

from helpers.selectFileFolder import selectFileFolder
from setDesktopAsDestFolder import setDesktopAsDestFolder

sys.path.append('./helpers')
from helpers.message import title, error


def setDestination():
    title('DESTINATION PATH (where to save the reports)')
    try: confirm = int(input('''> Destination path:
                        \n1. Set desktop
                        \n2. Set a particular folder
                        \n> '''))
    except: error("must select 1 or 2")
    if confirm == 1:
        destinationFolder = setDesktopAsDestFolder()
        if destinationFolder == False:
            destinationFolder = selectFileFolder('Destination')
    elif confirm == 2: destinationFolder = selectFileFolder('Destination')
    else: destinationFolder = setDestination()
    return destinationFolder