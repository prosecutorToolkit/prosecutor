import subprocess, json

def getVideoMetadata(file):
    try:
        command = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams', '-show_format', file]
        output = subprocess.check_output(command).decode('utf-8')
        metadata = json.loads(output)

        data = "Title: {}\nArtist: {}\nGenre: {}\nYear Released: {}\nBitrate: {} kbps\nComposer: {}\nFilesize: {} bytes\nAlbumArtist: {}\nDuration: {} seconds\nTrackTotal: {}".format(
            metadata['format']['tags'].get('title', ''),
            metadata['format']['tags'].get('artist', ''),
            metadata['format']['tags'].get('genre', ''),
            metadata['format']['tags'].get('date', ''),
            int(metadata['format']['bit_rate'])//1000 if metadata['format']['bit_rate'] else '',
            metadata['format']['tags'].get('composer', ''),
            metadata['format']['size'],
            metadata['format']['tags'].get('album_artist', ''),
            int(float(metadata['format']['duration'])),
            metadata['format']['tags'].get('track_total', '')
        )

    except: data = 'ERROR'

    return data