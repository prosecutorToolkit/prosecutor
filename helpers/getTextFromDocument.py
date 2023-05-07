import zipfile

def getTextFromDocument(file):
    with zipfile.ZipFile(file) as doc_zip:
        file_list = doc_zip.namelist()
        fileText = ''
        for f_name in file_list:
            if f_name.endswith('.xml'):
                with doc_zip.open(f_name) as f:
                    content = f.read().decode('utf-8')
                    fileText += content
        return fileText

# print(getTextFromDocument('/home/admin1/Downloads/Caso.docx'))