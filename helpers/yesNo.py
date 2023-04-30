import colorama
from message import error

def yesNo(question):
    while True:
        confirm = str(input(colorama.Fore.BLUE + '\n' + question))
        print(colorama.Style.RESET_ALL)
        if confirm == 'y' or confirm == 'Y':
            confirm = True
            break
        elif confirm == 'n' or confirm == 'N':
            confirm = False
            break
        else: error("must set 'y', 'n'. ID=YN")
    return confirm