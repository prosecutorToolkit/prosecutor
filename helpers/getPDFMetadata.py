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
        data += '\n' + str(key) + ': ' + str(value)
    return data


# print(getPDFMetadata('/home/admin1/Downloads/Notes App.pdf'))
# print(getPDFMetadata('/home/admin1/Downloads/Certificado Termux Hacking.pdf'))