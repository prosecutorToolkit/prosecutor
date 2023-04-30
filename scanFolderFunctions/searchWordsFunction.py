import sys

sys.path.append('./helpers')
from helpers.message import title, alert
from helpers.yesNo import yesNo


def searchWordsFunction():
    title('SEARCH WORDS (optional)')
    while True:
        searchWords = str(input("Introduce the search words sepparate by commas:\n> "))
        if len(searchWords) < 2:
            confirm = yesNo('''You have not introduced a search term. However you will get the text of the files in the target directory and subdirectorys
            \nAre you sure? (y/n)
            \n   > Yes, I want to get the report without any search
            \n   > No, I want to set some search terms
            \n> ''')
            if confirm == False: continue
            else:
                listofsearch = False
                break
        listofsearch = searchWords.split(',')
        xxl_term = False
        if len(listofsearch) > 0:   #Cleaning inputs and checking xxl terms 
            for i, value in enumerate(listofsearch):
                listofsearch[i] = str(value.strip())
                lengt = len(str(value))  #its sepparated in order to reduce the processing cost, with cost in RAM
                if lengt > 15: xxl_term = True
                elif lengt < 3:
                    listofsearch.remove(value)
                    alert("'{}' is a short value, search with this term could create crashes and it have been removed".format(value))
                    continue
        shownString = ""
        for searchTerm in listofsearch: shownString += '\n  > ' + str(searchTerm)
        if xxl_term:
            alert('You are setting extended words or phrases, this configuration in addition to admit misspellings could generate delays and high consume of CPU, that its discouraged.')
            confirm = yesNo('\nDo you want to continue? (y/n) \n > ')
            if not confirm: continue
        confirm = yesNo('Search terms: {}\nAre you sure that you want to search this terms? (y/n)\n > '.format(shownString))
        if not confirm: continue
        break
    return listofsearch