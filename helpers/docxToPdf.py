import platform, os
from message import success, error
from docx2pdf import convert
from docxToPdfUnix import docxToPdfUnix


def docxToPdf(path_docx, path_pdf):
    try:
        if platform.system() == 'Windows':
            convert(path_docx, path_pdf)
            pdfSuccess = True
        else:
            pdfSuccess = docxToPdfUnix(path_docx)

        success("PDF was created")

        if pdfSuccess:
            return True           # PDF created
        else: 
            return False          # PDF not created

    except:
        error("Cant create PDF")
        return False          # PDF not created