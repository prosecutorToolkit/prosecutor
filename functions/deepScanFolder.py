import sys, os

sys.path.append('./scanFolderFunctions')
from scanFolderFunctions.formatFile import formatFile
from scanFolderFunctions.setDataToGet import setDataToGet
from scanFolderFunctions.searchWordsFunction import searchWordsFunction
from scanFolderFunctions.misspellings import misspellings
from scanFolderFunctions.outputFiles import outputFiles
from scanFolderFunctions.setDestination import setDestination
from scanFolderFunctions.setJudicialDataCase import setJudicialDataCase
from scanFolderFunctions.processMatchWords import processMatchWords
from scanFolderFunctions.routeFiles import routeFiles
from scanFolderFunctions.readEngine import readEngine
from scanFolderFunctions.createReports import createReports
from helpers.sql import createScanReportTable

sys.path.append('./helpers')
from helpers.message import error, blue, show, success, title, yellow
from helpers.yesNo import yesNo
from helpers.selectFileFolder import selectFileFolder
from helpers.timeReport import timeReport
from helpers.merkleTree import merkleTree
from helpers.createHeader import header
from helpers.sql import saveHeaderInTable, saveIgnoredFilesInDB


def deepScanFolder():
    def __init__():
        errStr = ''
        while True:
            # try:
            errStr = 'selectFileFolder Target'
            targetFolder = selectFileFolder("Target")

            errStr = 'formatFile'
            formatsListInObj = formatFile()

            errStr = 'setDataToGet'
            dataToGetObject = setDataToGet()

            errStr = 'searchWordsFunction'
            listOfSearch = searchWordsFunction()

            if listOfSearch:
                errStr = 'listOfSearch'
                shownQuery = ''
                for term in listOfSearch: shownQuery += "\n    - " + term

                errStr = 'misspellings'
                misspellingsObject = misspellings()

            errStr = 'outputFiles'
            outputFilesObject = outputFiles()

            errStr = 'setDestination'
            destinationFolder = setDestination()

            errStr = 'setJudicialDataCase'
            caseData = setJudicialDataCase()

            while True:
                def text(listOfSearch):
                    blue('\nCONFIGURATION:')
                    show('1. Target folder:', targetFolder)
                    show('2. Data to get:', dataToGetObject.string)
                    show('3. Format files:', formatsListInObj.string)
                    show('4. Search term (optional):', shownQuery)
                    if listOfSearch:
                        show('5. Misspellings (optional):', misspellingsObject.string)
                    blue('REPORT:')
                    show('6. Output files:', outputFilesObject.string)
                    show('7. Destination folder:', destinationFolder)
                    show('8. Judicial Data Case:', caseData)

                errStr = 'text function num 1'
                text(listOfSearch)
                confirm = yesNo('\nDo you want to confirm this configuration and start scan? (y/n)\n > ')
                if confirm: break
                else:
                    while True:
                        errStr = 'update'
                        try:
                            errStr = 'text function num 2'
                            text(listOfSearch)
                            print('\n9. CLEAN ALL\n10. NONE: START SCAN')
                            blue('\nWhat do you want to update?')
                            update = int(input(' > '))
                            if update < 1 or update > 10:
                                error('must select a valid number. ID=S6')
                                blue('ENTER to try again')
                                option = input(' > ')
                                continue
                        except:
                            error('must select a number. ID=S7')
                            continue
                        if update == 1: targetFolder = selectFileFolder("Target")
                        elif update == 2: dataToGetObject = setDataToGet()
                        elif update == 3: formatsListInObj = formatFile()
                        elif update == 4:
                            listOfSearch = searchWordsFunction()
                            shownQuery = ''
                            for term in listOfSearch: shownQuery += "\n    - " + term
                        elif update == 5 and not listOfSearch:
                            error('You have not introduce a search term. This option is not available. ID=10')
                        elif update == 5 and listOfSearch: misspellingsObject = misspellings()
                        elif update == 6: outputFilesObject = outputFiles()
                        elif update == 7: destinationFolder = setDestination()
                        elif update == 8: caseData = setJudicialDataCase()
                        elif update == 9: __init__()
                        else: break

        ################# START #####################

            if listOfSearch:
                title('Processing inputs')
                errStr = 'processMatchWords'
                listOfSearch = processMatchWords(listOfSearch, misspellingsObject)
                if not listOfSearch: break
            else: yellow('There are no inputs setted to process')

            errStr = 'routeFiles'
            filesRouteList, ignoredFilesList = routeFiles(formatsListInObj, targetFolder)

            if not filesRouteList:
                error('The target folder havent files to scan. ID=S13')
                break

            errStr = 'timeReport'
            time_report = timeReport()
        
            filePath = os.path.join(destinationFolder, 'Prosecutor report ' + time_report)

            errStr = 'shownQuery'
            shownQuery = shownQuery.replace('\n', ' ')
            while '  ' in shownQuery: shownQuery = shownQuery.replace('  ', ' ')

            errStr = 'merkleTree'
            mercle = str(merkleTree(targetFolder))

            errStr = 'Head class'
            headObj = header(time_report, caseData, targetFolder, mercle, formatsListInObj.strInLine, shownQuery, misspellingsObject.strInLine)

            sqlFilePath = filePath + '.db'
            createScanReportTable(sqlFilePath)

            errStr = 'Save header in DB'
            data = (time_report, caseData, targetFolder, mercle, formatsListInObj.strInLine, shownQuery, misspellingsObject.strInLine)
            saveHeaderInTable(sqlFilePath, data)

            saveIgnoredFilesInDB(sqlFilePath, ignoredFilesList)

            errStr = 'Read engine'
            listOfData = readEngine(dataToGetObject, filesRouteList, listOfSearch, sqlFilePath)
            if listOfData:
                success('The files have been readed!')
            else:
                error('Unknown. Cant read the files. ID=S11')

            errStr = 'createReports'
            reports = createReports(sqlFilePath, filePath, outputFilesObject, headObj, listOfData, ignoredFilesList)
            if reports: success('The report/s have been created! 😎')
            else: error('Unknown. Cant create the report. ID=S12')

            # except:
            #     error('scanFolder ' + errStr)
            
            break

    __init__()