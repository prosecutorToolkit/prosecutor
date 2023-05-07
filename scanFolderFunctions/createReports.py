import sys, os, zipfile

sys.path.append('./helpers')
from helpers.message import success, error
from helpers.createExcelFile import createExcelFile
from helpers.createDocxFile import createDocxFile
from helpers.createCSVFile import createCSVFile
from helpers.docxToPdf import docxToPdf
from helpers.sql import getScanReportData, getHeaderFromSQL, getIgnoredFilesData
from helpers.createHeader import header


# def createReports(sqlFilePath, filePath, outputFilesObject, headObj=None, listOfData=None):
def createReports(sqlFilePath, filePath, outputFilesObject, headObj=None, listOfData=None, ignoredFilesList=None):

    if listOfData == None:
        listOfData = getScanReportData(sqlFilePath)
        headerData = getHeaderFromSQL(sqlFilePath)
        headerData = headerData[0]
        headObj = header(headerData[0], headerData[1], headerData[2], headerData[3], headerData[4], headerData[5], headerData[6])
        filePath += ' Data getted at ' + headerData[0]  # TIME_REPORT
        ignoredFilesList = getIgnoredFilesData(sqlFilePath)

    # try:

    print("Creating report...")

    list_to_zip = []

    # Create CSV
    if outputFilesObject.csv:
        path_csv = filePath + '.csv'
        successTask = createCSVFile(path_csv, listOfData, headObj)
        if successTask: list_to_zip.append(path_csv)
    
    # Create Doc / Docx
    if outputFilesObject.doc or outputFilesObject.pdf:
        path_docx = filePath + '.docx'
        docxSuccessTask = createDocxFile(path_docx, listOfData, headObj)
        if docxSuccessTask:
            if outputFilesObject.doc:
                list_to_zip.append(path_docx)
            if outputFilesObject.pdf:
                path_pdf = filePath + '.pdf'
                pdfSuccessTask = docxToPdf(path_docx, path_pdf)
                if pdfSuccessTask:
                    list_to_zip.append(path_pdf)
        if not outputFilesObject.doc:
            os.remove(path_docx)
            success("Docx was removed")

    # Create Xlsx
    if outputFilesObject.xlsx:
        path_xlsx = filePath + '.xlsx'
        successTask = createExcelFile(path_xlsx, listOfData, headObj, ignoredFilesList)
        if successTask:
            list_to_zip.append(path_xlsx)
    
    if outputFilesObject.sql:
        list_to_zip.append(sqlFilePath)
        print('SQL append to zip list')
    else:
        os.remove(sqlFilePath)
        print('SQL file was removed')

    # Compress outputs files
    if outputFilesObject.zip:
        folder_zip = filePath + ".zip"
        zipF = zipfile.ZipFile(folder_zip, 'w')
        for value in list_to_zip:
            try:
                zipF.write(value, arcname=os.path.basename(value), compress_type=zipfile.ZIP_DEFLATED)
                os.remove(value)
            except: error(f'Cant compress/remove in Zip the file {value}')
        zipF.close()

        success('Zip was created')
    
    print('Reports created successfully!')
    return True

    # else: False