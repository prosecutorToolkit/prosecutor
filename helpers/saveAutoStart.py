import sys

sys.path.append('../helpers')
from helpers.message import success

def saveAutoStart(key, option):
    add = False
    with open("conf.py", 'rt') as file:
        lines = file.readlines()
    with open("conf.py", 'wt') as file:
        for line in lines:
            if line.startswith(key):
                if option == 0: file.write("")
                else:
                    file.write("{}'{}'".format(key, option))
                    add = True
            else:
                file.write(line)
        if option:
            if not add: file.write("{}'{}'".format(key, option))
    success("Saved!")