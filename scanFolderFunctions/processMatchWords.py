import sys

sys.path.append('./helpers')
from helpers.message import error
from helpers.misspellingsHelpers import indifferent, one_letter_indifferent, get_upper_and_lower

def processMatchWords(listOfSearch, misspellingsObject):
    strOfSearchTerms = ''
    for term in listOfSearch: strOfSearchTerms += ',' + str(term)
    
    try:
        errorValue = 'misspellingsObject.BV'
        if misspellingsObject.BV:
            strOfSearchTerms = indifferent(strOfSearchTerms,"v","b")

        errorValue = 'misspellingsObject.GJ'
        if misspellingsObject.GJ:
            strOfSearchTerms = indifferent(strOfSearchTerms,"g","j")

        errorValue = 'misspellingsObject.H'
        if misspellingsObject.H:
            strOfSearchTerms = one_letter_indifferent(strOfSearchTerms, "h")

        errorValue = 'misspellingsObject.U'
        if misspellingsObject.U:
            strOfSearchTerms = one_letter_indifferent(strOfSearchTerms, "u")

        listOfSearchTerms = strOfSearchTerms.split(',')

        # elimina strings vacios que se agregaron tras las funciones de misspellings
        listOfSearchTerms = list(filter(lambda x: x != "", listOfSearchTerms))

        return listOfSearchTerms

    except:
        error(errorValue)
        return False