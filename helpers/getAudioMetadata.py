from tinytag import TinyTag

def getAudioMetadata(file):
    audio = TinyTag.get(file)
    return f"""Title: {str(audio.title)}
Artist: {str(audio.artist)}
Genre: {str(audio.genre)}
Year Released: {str(audio.year)}
Bitrate: {str(audio.bitrate)} kBits/s
Composer: {str(audio.composer)}
Filesize: {str(audio.filesize)} bytes
AlbumArtist: {str(audio.albumartist)}
Duration: {str(audio.duration)} seconds
TrackTotal: {str(audio.track_total)}"""

# print(getAudioMetadata('/home/admin1/Downloads/8CadnxQnMIA_48.mp3'))

# decime si este código requiere alguna corrección:

# from tinytag import TinyTag

# def getAudioMetadata(file):
#     audio = TinyTag.get(file)
#     data = "Title:" + audio.title + "\nArtist: " + audio.artist + "\nGenre:" + audio.genre + "\nYear Released: " + audio.year + "\nBitrate:" + str(audio.bitrate) + "kBits/s\nComposer: " + audio.composer + "\nFilesize: " + str(audio.filesize) + " bytes\nAlbumArtist: " + audio.albumartist + "\nDuration: " + str(audio.duration) + " seconds\nTrackTotal: " + str(audio.track_total)
#     return data