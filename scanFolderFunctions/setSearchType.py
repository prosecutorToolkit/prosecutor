import sys

sys.path.append('./helpers')
from helpers.message import error, yellow

def setSearchType():
    while True:
        option = input('''Do you want to search in the folder?
        t. Yes, by search terms
        r. Yes, by regular expression
        n. No
        \n > ''')
        if option == 't':
            yellow('You set search by search terms')
            return 1
        elif option == 'r':
            yellow('You set search by regular expression')
            return 2
        elif option == 'n':
            yellow('You set no search')
            return False
        else:
            error('Invalid option. ID=SST')