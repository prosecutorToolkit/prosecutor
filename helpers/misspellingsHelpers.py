import itertools
from itertools import product

def indifferent(listOfSearch, letter1, letter2):
    letter1_upper = letter1.upper()
    letter2_upper = letter2.upper()
    letter1_lower = letter1.lower()
    letter2_lower = letter2.lower()
    position = 0
    listOfSearch = listOfSearch.split(',')
    newletter = False
    new_string = ""
    for searchTerm in listOfSearch:
        vb = 0
        for letter in searchTerm:
            if letter == letter1_upper or letter == letter2_upper or letter == letter1_lower or letter == letter2_lower: vb +=1
        if vb > 0:
            vblist_by_term = [''.join(i) for i in itertools.product([letter1_lower, letter2_lower], repeat = vb)]
            vb_list_by_Letter = []
            for value1 in vblist_by_term:
                for letter1 in value1: vb_list_by_Letter.append(letter1)
            position = 0
            for variation in vblist_by_term:
                string = ""
                for letter in searchTerm:
                    newletter = False
                    if letter == letter1_upper or letter == letter2_upper or letter == letter1_lower or letter == letter2_lower:
                        vbvalue = vb_list_by_Letter[position]
                        position += 1
                        newletter = True
                    if newletter == True: string += vbvalue
                    else: string += letter
                new_string += string + ","
        else: new_string += searchTerm + ","
    return new_string[:-1]


def get_upper_and_lower(string):
    try: listOfSearch = string.split(',')
    except:
        listOfSearch = list()
        listOfSearch.append(string)
    return_string = ""
    for term in listOfSearch:
        strip_term = term.strip()
        result = map(''.join, product(*((c.lower(), c.upper()) for c in strip_term)))
        for variation in result:
            return_string += variation + ","
    return return_string


def one_letter_indifferent(string, letter1):
    string = string.replace("&", '-')
    letter2 = "&"
    letter1_upper = letter1.upper()
    letter1_lower = letter1.lower()
    try: listOfSearch = string.split(',')
    except:
        listOfSearch = list()
        listOfSearch.append(string)
    for searchTerm in listOfSearch:
        newvalue = searchTerm.strip()
        index = listOfSearch.index(searchTerm)
        listOfSearch[index] = newvalue
    position = 0
    string = ""
    newletter = False
    newletter = False
    new_string = ""
    for searchTerm in listOfSearch:
        vb = 0
        for letter in searchTerm:
            if letter == letter1_upper or letter == letter1_lower: vb +=1
        if vb > 0:
            vblist_by_term = [''.join(i) for i in itertools.product([letter1_lower, letter2], repeat = vb)]
            vb_list_by_Letter = []
            for value1 in vblist_by_term:
                for letter1 in value1: vb_list_by_Letter.append(letter1)
            position = 0
            for variation in vblist_by_term:
                for letter in searchTerm:
                    newletter = False
                    if letter == letter1_upper or letter == letter1_lower or letter == letter2:
                        vbvalue = vb_list_by_Letter[position]
                        position += 1
                        newletter = True
                    if newletter == True: string += vbvalue
                    else: string += letter
                new_string += string + ","
                string = ""
        else: new_string += searchTerm + ","
        new_string = new_string.replace("&", "")
    return new_string[:-1]
