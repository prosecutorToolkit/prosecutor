import sys, ntpath, re

sys.path.append('./helpers')
from helpers.message import title
from helpers.extractMetadata import extractMetadata
from helpers.getsha256file import getsha256file
from helpers.searchInList import searchInList
from helpers.readText import readText


def readEngine(dataToGetObject, filesRouteList, listOfSearch):
    listOfData = []
    idF = 0
    totalFiles = len(filesRouteList)
    intValue = (1/totalFiles) * 100
    progress = 0

    title("Starting read engine...")

    for file in filesRouteList:
        idF += 1
        name = ntpath.basename(file)
        text = ''

        # No se aplica nuevo filtro de formato deseado porque eso ya fue filtrado al listar los archivos
        if dataToGetObject.text or listOfSearch:
            text = readText(file)

        if dataToGetObject.metadata: metadataF = extractMetadata(file)
        else: metadataF = ''

        if dataToGetObject.hash: hashF = getsha256file(file)
        else: hashF = ''

        if dataToGetObject.path: pathF = file
        else: pathF = ''

        matchF = ''
        if listOfSearch:
            matchF += ' ' + searchInList(listOfSearch, metadataF)
            matchF += ' ' + searchInList(listOfSearch, text)

        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', ' ', text) # reemplazar caracteres no permitidos por espacios en blanco

        if not dataToGetObject.text: text = ''

        listOfData.append((idF, name, pathF, hashF, matchF, text, metadataF))

        progress += intValue
        sys.stdout.write(f"\rProgress: {round(progress, 2)}%  | Files: {idF}/{totalFiles}\n")
        sys.stdout.flush()

    return listOfData