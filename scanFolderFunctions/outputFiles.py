# CAMBIAR RAR a ZIP

import sys

sys.path.append('./helpers')
from helpers.message import title, error
from helpers.yesNo import yesNo


def outputFiles():
    title('REPORT/S TO CREATE')
    while True:
        document_file = False; spreadsheet_file = False; pdf_file = False; csv_file = False; zip_file = False
        shownString = ''

        try:
            flags = input('''Set the config flags:
            \n  - a (get all: document, spreadsheet, PDF and CSV, all compressed in a ZIP file)
            \n  - d (document: docx)
            \n  - s (spreadsheet: xlsx)
            \n  - p (portable document format: PDF)
            \n  - c (commas sepparate values: csv)
            \n  - z (compress output in a ZIP file)
            \n > ''')
            if len(flags) == 0:
                error("must select at least one flag")
                continue
            flags = list(flags)
            if 'a' in flags:
                confirm = yesNo('Are you sure that you want to get All (document, PDF, etc. in ZIP)? (y/n)\n> ')
                if confirm == True:
                    document_file = True
                    spreadsheet_file = True
                    pdf_file = True
                    csv_file = True
                    zip_file = True
                    shownString = '''\n  > Document
                                     \n  > CSV file
                                     \n  > Spreadsheet
                                     \n  > PDF
                                     \n  > Compressed in a ZIP file'''

            else:
                if 'd' in flags:
                    document_file = True
                    shownString += '\n  > Document'
                if 'c' in flags:
                    csv_file = True
                    shownString += '\n  > CSV file'
                if 's' in flags:
                    spreadsheet_file = True
                    shownString += '\n  > Spreadsheet'
                if 'p' in flags:
                    pdf_file = True
                    shownString += '\n  > PDF'
                if 'z' in flags:
                    zip_file = True
                    shownString += '\n  > Compressed in a ZIP file'
                
                if zip_file == True and document_file == False and spreadsheet_file == False and pdf_file == False and csv_file == False:
                    error("You must select at least one output type. Zip isn't a output file, this option can compress the selected output files (example: PDF, CSV, etc.). ID=S3")
                    continue

                confirm = yesNo('Selected items:{}\nAre you sure that you want to get these items? (y/n)\n> '.format(shownString))
                if not confirm: continue

            print('shownString:\n' + shownString)

            def configure():
                class Config:
                    def __init__(self):
                        self.string = shownString
                        self.doc = document_file
                        self.xlsx = spreadsheet_file
                        self.pdf = pdf_file
                        self.csv = csv_file
                        self.zip = zip_file
                return Config

            getConfig = configure()

        except:
            error("Unknown. ID=S2")

        break

    return getConfig()