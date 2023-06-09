import os

from getPDFMetadata import getPDFMetadata
from getImageMetadata import getImageMetadata
from getVideoMetadata import getVideoMetadata
from getAudioMetadata import getAudioMetadata

def extractMetadata(file):
    ext = os.path.splitext(file)[1].lower()
    data = ''
    if ext == '.pdf':
        try: data = getPDFMetadata(file)
        except: data = 'Cant get metadata'
    elif ext == '.txt':
        return ' '  # this type of file hasnt metadata
    else:
        try: data = getAudioMetadata(file)
        except:
            try: data = getImageMetadata(file)
            except:
                try: data = getVideoMetadata(file)
                except: data = 'Cant get metadata'
    return data