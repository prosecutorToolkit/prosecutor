import sys, os

sys.path.append('./scanFolderFunctions')
from scanFolderFunctions.setDestination import setDestination
from scanFolderFunctions.createReports import createReports
from scanFolderFunctions.outputFiles import outputFiles

sys.path.append('./helpers')
from helpers.message import success, error
from helpers.selectFileFolder import selectFileFolder
from helpers.timeReport import timeReport
from helpers.timeReport import timeReport


def createReportsFromDB():
    # try:

    errStr = 'selectFileFolder File'
    sqlFilePath = selectFileFolder("DB")

    errStr = 'setDestination'
    destinationFolder = setDestination()

    outputFilesObject = outputFiles()

    filePath = os.path.join(destinationFolder, 'Prosecutor report ' + 'built at ' + timeReport())

    createReports(sqlFilePath, filePath, outputFilesObject)

    success('Reports created from database successfully!')

    # except:
    #     error(errStr)