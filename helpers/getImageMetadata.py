from PIL import Image as img
from PIL.ExifTags import TAGS, GPSTAGS

def getImageMetadata(file):
    image = img.open(file)
    
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }
    
    # Extract EXIF metadata
    exifdata = image.getexif()
    if exifdata:
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                try: data = data.decode()
                except UnicodeDecodeError: data = str(data)
            info_dict[tag] = data
    
    # Extract GPS metadata
    exifgps = exifdata.get(34853, {})
    if isinstance(exifgps, dict):
        for key in exifgps:
            gps_tag = GPSTAGS.get(key, key)
            info_dict[gps_tag] = exifgps[key]
    
    # Extract IPTC metadata
    iptcdata = image.info.get('iptc', {})
    if iptcdata:
        for key in iptcdata:
            info_dict[key] = iptcdata[key][0]
    
    # Extract XMP metadata
    xmpdata = image.info.get('xmp', {})
    if xmpdata:
        for key in xmpdata:
            info_dict[key] = xmpdata[key]
    
    # Convert dictionary to string
    data = ""
    for label, value in info_dict.items():
        data += f"{label}: {value}\n"
    
    return data

# print(getImageMetadata('/media/veracrypt5/5_INFORMATICA/1_PROGRAMMING/2_MY_PROGRAMS/AnalizadorDeExtraccionUFED/PARA_DATIP/FINAL/SCANPRUEBA/wp2579098.jpg'))