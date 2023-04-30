import sys

sys.path.append('./helpers')
from helpers.message import error, yellow, blue
from helpers.downloadYoutubeVideo import downloadYoutubeVideo
from helpers.askPath import askPath

def getYoutubeVideo():
    yellow('\n*Prosecutor download videos at top quality available')

    while True:
        blue('Set the YouTube link:')
        link = str(input(' > '))
        if 'youtube' in link or 'Youtube' in link or 'YouTube'in link: break
        else: error('Invalid link. Make sure that you set a youtube link (case sentitive)')
    blue('\nSet where you want to save the video:')
    path = askPath()
    
    print(f'\nThe video will be downloaded at: {path}')
    
    downloadYoutubeVideo(link, path)