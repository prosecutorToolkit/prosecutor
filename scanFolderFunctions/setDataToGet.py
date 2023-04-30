import sys

sys.path.append('./helpers')
from helpers.message import title, error
from helpers.yesNo import yesNo


def setDataToGet():
    title('DATA TO GET FROM ALL THE FILES')
    while True:
        getText = False; getMetadata = False; getHash = False; getPath = False
        shownString = ''

        flags = str(input('''Set the type of data to get:    (example: ph)
            \n  > a (get all: text, path, metadata and hash)
            \n  > t (text)
            \n  > p (path)
            \n  > m (metadata)
            \n  > h (hash sha-256)
            \n*Also Prosecutor get filenames, match (if it does) and ignored files (if the format is not target or its unavailable)
            \n> '''))
        
        if not flags:
            error("must select at least one type of data to get")
            continue
        
        flags = list(flags.lower())
        
        if 'a' in flags:
            confirm = yesNo('\nAre you sure that you want to get All (text, path, metadata and hash)? (y/n)\n > ')
            if confirm == True:
                getText = True
                getPath = True
                getMetadata = True
                getHash = True
                shownString = '''\n  > text
                                 \n  > path
                                 \n  > metadata
                                 \n  > hash'''
        else:
            if 't' in flags:
                getText = True
                shownString += '\n  > text'
            if 'p' in flags:
                getPath = True
                shownString += '\n  > path'
            if 'm' in flags:
                getMetadata = True
                shownString += '\n  > metadata'
            if 'h' in flags:
                getHash = True
                shownString += '\n  > hash'
            confirm = yesNo('Selection: {}\nAre you sure that you want to get this data from files? (y/n)\n > '.format(shownString))
            if confirm == False: continue
        def data():
            class DataGet:
                def __init__(self):
                    self.string = shownString
                    self.text = getText
                    self.metadata = getMetadata
                    self.hash = getHash
                    self.path = getPath
            return DataGet
        getData = data()
        break
    return getData()