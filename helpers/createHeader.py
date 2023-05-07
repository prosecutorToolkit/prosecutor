import os

def header(time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString, regex):
    class Head:
        def __init__(self, time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString, regex):
            self.user = "> User: " + os.getlogin()
            self.time = "> Date time: " + time_report
            self.case = "> Case data: " + caseData
            self.target = "> Main target folder: " + targetFolder
            self.mercle = "> Hash of folder: " + mercle
            self.formats = "> Format search: " + formatsListInObjString
            if misspellingsObjectString:
                self.terms = "> Search terms: " + shownQuery
                self.misspellings = "> Include spelling variations: " + misspellingsObjectString
            else:
                self.misspellings = False
                self.terms = False
            if regex:
                self.regex = "> Search with regular expression: " + regex
            else:
                self.regex = False

    return Head(time_report, caseData, targetFolder, mercle, formatsListInObjString, shownQuery, misspellingsObjectString, regex)