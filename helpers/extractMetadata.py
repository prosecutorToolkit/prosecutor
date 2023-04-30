import os

from getPDFMetadata import getPDFMetadata
from getImageMetadata import getImageMetadata
from getVideoMetadata import getVideoMetadata
from getAudioMetadata import getAudioMetadata

def extractMetadata(file):
    ext = os.path.splitext(file)[1]
    data = ''
    if ext == '.pdf':
        try: data = getPDFMetadata(file)
        except: data = 'Cant get metadata'
    else:
        try: data = getAudioMetadata(file)
        except:
            try: data = getImageMetadata(file)
            except:
                try: data = getVideoMetadata(file)
                except: data = 'Cant get metadata'
    return data

# print(extractMetadata('/home/admin1/Downloads/8CadnxQnMIA_48.mp3'))
# print(extractMetadata('/home/admin1/Downloads/Android Studio Install in Linux.mp4'))