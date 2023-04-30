import sys, os
from pytube import YouTube

sys.path.append('./helpers')
from helpers.message import success, error, show, yellow
from helpers.launchFile import launchFile
from helpers.yesNo import yesNo
from helpers.getVideoMetadata import getVideoMetadata
from helpers.getsha256file import getsha256file

def downloadYoutubeVideo(link, savePath):
    try:
        strError = 'yt'
        yt = YouTube(link)  # Create a YouTube object

        strError = 'video_stream'
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()  # Get the best image quality available

        yellow('\nDownloading, please wait')

        strError = 'download'
        video_stream.download(output_path=savePath, filename=yt.title) # Dowload the video

        strError = 'data'

        success('\nThe video was downloaded successfuly!')

        fileRoute = os.path.join(savePath, yt.title)

        try: metadata = getVideoMetadata(fileRoute)
        except: error('cant extract metadata')

        hashF = getsha256file(fileRoute)
        if hashF == 'ERROR': error('cant hash this file')

        show('\nHASH SHA-256:', hashF)
        print('\nDATA:')
        show('  > Title: ', yt.title)
        show('  > ID: ', yt.video_id)
        show('  > Rating: ', yt.rating)
        show('  > Views: ', yt.views)
        show('  > Length: ', yt.length)
        show('  > Description: ', yt.description)
        show('\nMETADATA:', metadata)

        strError = 'launch'
        confirm = yesNo('\nDo you want to launch the video?\n > ')
        if confirm: launchFile(fileRoute)

    except:
        error('\nCant download. Possible causes: There are not internet connection or the folder where you want to save the file require administrator privileges. ID={}.'.format(strError))