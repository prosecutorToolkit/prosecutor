import re

# This function search a list of inputs in a given text
def searchInList(listOfSearch, text):
    matchF = ''
    
    for searchTerm in listOfSearch:
        if re.search(searchTerm, text, re.IGNORECASE):
            matchF = str(searchTerm)
            break
    
    return matchF