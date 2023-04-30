import colorama

def error(inputValue = "Unknown error. ID=DE"):
    print(colorama.Fore.RED + 'x ERROR: {}'.format(inputValue))
    print(colorama.Style.RESET_ALL)

def success(inputValue = ""):
    print(colorama.Fore.GREEN + 'x Success! {}'.format(inputValue))
    print(colorama.Style.RESET_ALL)


def alert(inputValue = ""):
    print(colorama.Fore.MAGENTA + '¡! ALERT!: {}'.format(inputValue))
    print(colorama.Style.RESET_ALL)

def title(inputValue):
    print(colorama.Fore.CYAN + '\n' + str(inputValue))
    print(colorama.Style.RESET_ALL)

def red(inputValue):
    print(colorama.Fore.RED + str(inputValue))
    print(colorama.Style.RESET_ALL)

def green(inputValue):
    print(colorama.Fore.GREEN + str(inputValue))
    print(colorama.Style.RESET_ALL)

def blue(inputValue):
    print(colorama.Fore.BLUE + str(inputValue))
    print(colorama.Style.RESET_ALL)

def yellow(inputValue):
    print(colorama.Fore.YELLOW + str(inputValue))
    print(colorama.Style.RESET_ALL)

def show(title, options):
    print(title)
    yellow(options)

