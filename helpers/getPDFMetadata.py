from pdfreader import SimplePDFViewer

def getPDFMetadata(file):
    fd = open(file, "rb")
    viewer = SimplePDFViewer(fd)
    data = ''
    for key, value in viewer.metadata.items():
        if isinstance(value, bytes):
            try: value = value.decode('utf-8')
            except:
                try: value = value.decode('utf-16')
                except: value = value.decode('utf-32')
        data += str(key) + ': ' + str(value) + '\n'
    return data