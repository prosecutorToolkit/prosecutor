import sys, ntpath, re, time, os

sys.path.append('./helpers')
from helpers.message import title, yellow
from helpers.extractMetadata import extractMetadata
from helpers.getsha256file import getsha256file
from helpers.searchInList import searchInList
from helpers.readText import readText
from helpers.searchWithRegEx import searchWithRegEx

def secsToTime(s):
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    s = round(s % 60, 2)
    if h > 0: return f'{h} Hs. {m} Min. {s} Sec.'
    elif m > 0: return f'{m} Min. {s} Sec.'
    else: return f'{s} Sec.'

def readEngine(dataToGetObject, filesRouteList, listOfSearch, regex):
    listOfData = []
    idF = 0
    totalFiles = len(filesRouteList)
    intValue = (1/totalFiles) * 100
    progress = 0
    acumuledTime = 0

    title("Starting read engine...")

    start_time = time.time()

    for file in filesRouteList:
        fileStartTime = time.time()
        idF += 1
        name = ntpath.basename(file)
        text = ''

        if dataToGetObject.text or listOfSearch:
            text = readText(file)

        if dataToGetObject.metadata: metadataF = extractMetadata(file)
        else: metadataF = ''

        if dataToGetObject.hash: hashF = getsha256file(file)
        else: hashF = ''

        if dataToGetObject.path: pathF = os.path.dirname(file)
        else: pathF = ''

        matchF = ''
        cutText = ''
        if listOfSearch:
            matchF, cutText = searchInList(listOfSearch, text)
            matchF2, cutText2 = searchInList(listOfSearch, metadataF)
            matchF += matchF2
            cutText += cutText2
        if regex:
            matchF = searchWithRegEx(regex, text)
                # Is not available search with searchTerm and RegEx, about that it assign directly with =, ignoring if listOfSearch assign values inside (not use +=)

        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', ' ', text)
        # replace characters not not allowed with white spaces

        if not dataToGetObject.text: text = ''

        listOfData.append((idF, name, pathF, hashF, matchF, cutText, text, metadataF))

        progress += intValue
        acumuledTime += time.time() - fileStartTime
        sys.stdout.write(f"\rProgress: {round(progress, 2)}%  |  Files: {idF}/{totalFiles}  |  Remaining time: {secsToTime(acumuledTime / idF * (totalFiles - idF))}")
        sys.stdout.flush()

        # import psutil
        # if psutil.virtual_memory().percent > 85:
        #     saveSQL(sqlFilePath, listOfData)
        #     listOfData = []
        # This function is not available right now about it clean listOfData list.
        # To use this functionality I set the saveSQL inside this file (readEngine) and no inside the top file (deepScanFolder).

    end_time = time.time()

    yellow(f"\n\nTotal processing time: {secsToTime(end_time - start_time)}\n")

    return listOfData