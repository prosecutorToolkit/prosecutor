import sys, os, zipfile, ntpath

sys.path.append('./helpers')
from helpers.message import success, error, green
from helpers.createExcelFile import createExcelFile
from helpers.createDocxFile import createDocxFile
from helpers.createCSVFile import createCSVFile
from helpers.docxToPdf import docxToPdf
from scanFolderFunctions.sql import getScanReportData, getHeaderFromSQL, getIgnoredFilesData
from helpers.createHeader import header
from helpers.getsha256file import getsha256file

sys.path.append('./scanFolderFunctions')
from scanFolderFunctions.sql import createScanReportTable, saveSQL, saveIgnoredFilesInDB, saveHeaderInTable

# def createReports(sqlFilePath, filePath, outputFilesObject, headObj=None, listOfData=None):
def createReports(filePath, outputFilesObject, sqlFilePath, headObj=None, listOfData=None, ignoredFilesList=None, reportData=None, time_report=None):
    # try:
    list_to_zip = []

    global idL
    idL = 0
    def showFileData(file):
        global idL
        idL+=1
        if idL == 1:
            green(f'\nREPORT/S CREATED:\n- User: {os.getlogin()}\n- Time: {time_report}\n- Output folder: {os.path.dirname(file)}')
        green(f'> Report N°{idL}\n- File: {ntpath.basename(file)}\n- Hash sha-256: {getsha256file(file)}\n')

    if listOfData == None:
        print("Reading data...")
        listOfData = getScanReportData(sqlFilePath)
        headerData = getHeaderFromSQL(sqlFilePath)
        headerData = headerData[0]
        headObj = header(headerData[0], headerData[1], headerData[2], headerData[3], headerData[4], headerData[5], headerData[6], False)
        filePath += ' Data getted at ' + headerData[0]  # TIME_REPORT
        time_report = headerData[0]
        ignoredFilesList = getIgnoredFilesData(sqlFilePath)
    else:
        if outputFilesObject.sql:
            print("Creating report/s...")
            print("Creating database...")
            sqlFilePath = filePath + '.db'
            createScanReportTable(sqlFilePath)
            saveSQL(sqlFilePath, listOfData)
            saveIgnoredFilesInDB(sqlFilePath, ignoredFilesList)
            saveHeaderInTable(sqlFilePath, reportData)
            list_to_zip.append(sqlFilePath)
            showFileData(sqlFilePath)
        else:
            print("Creating report/s...")

    # Create CSV
    if outputFilesObject.csv:
        path_csv = filePath + '.csv'
        successTask = createCSVFile(path_csv, listOfData, headObj)
        if successTask:
            list_to_zip.append(path_csv)
            showFileData(path_csv)
    
    # Create Doc / Docx
    if outputFilesObject.doc or outputFilesObject.pdf:
        path_docx = filePath + '.docx'
        docxSuccessTask = createDocxFile(path_docx, listOfData, headObj)
        if docxSuccessTask:
            if outputFilesObject.doc:
                list_to_zip.append(path_docx)
                showFileData(path_docx)
            if outputFilesObject.pdf:
                path_pdf = filePath + '.pdf'
                pdfSuccessTask = docxToPdf(path_docx, path_pdf)
                if pdfSuccessTask:
                    list_to_zip.append(path_pdf)
                    showFileData(path_pdf)
        if not outputFilesObject.doc:
            os.remove(path_docx)
            # success("Docx was removed")

    # Create Xlsx
    if outputFilesObject.xlsx:
        path_xlsx = filePath + '.xlsx'
        successTask = createExcelFile(path_xlsx, listOfData, headObj, ignoredFilesList)
        if successTask:
            list_to_zip.append(path_xlsx)
            showFileData(path_xlsx)

    # success('Report/s created successfully!\n')

    # Compress outputs files
    if outputFilesObject.zip:
        path_zip = filePath + ".zip"
        zipF = zipfile.ZipFile(path_zip, 'w')
        for value in list_to_zip:
            try:
                zipF.write(value, arcname=os.path.basename(value), compress_type=zipfile.ZIP_DEFLATED)
            except:
                error(f'Cant compress in Zip the file {value}\n')
            try: 
                os.remove(value)
            except:
                error(f'Cant remove the file {value}\n')
        zipF.close()
        # success('Zip was created')

        if idL == 1: s = ''
        else: s = 's'
        green(f'Report{s} compressed at:\n- File: {ntpath.basename(path_zip)}\n- Hash sha-256: {getsha256file(path_zip)}\n')

    return True

    # else: False