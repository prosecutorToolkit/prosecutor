import os

def header(time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString):
    class Head:
        def __init__(self, time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString):
            self.user = "> User: " + os.getlogin()
            self.time = "> Date time: " + time_report
            self.case = "> Case data: " + caseData
            self.target = "> Main target folder: " + targetFolder
            self.mercle = "> Hash of folder: " + mercle
            self.formats = "> Format search: " + formatsListInObjString
            self.terms = "> Search terms: " + shownQuery
            self.misspellings = "> Include spelling variations: " + misspellingsObjectString

    return Head(time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString)