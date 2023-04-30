# from message import success, error

# def setApiKey():
#     while True:
#         apiKey = input("Introduce the API Key of Virus Total\n> ")
#         if len(apiKey) > 10:
#             write = False
#             file = open("conf.py", 'rw')
#             for line in file:
#                 if line.startswith('vt_api_key='):
#                     line.write("\nvt_api_key='{}'".format(apiKey))
#                     write = True
#             if not write:
#                 file.write("\nvt_api_key='{}'".format(apiKey))
#             file.close()
#             success('Done!')
#             break
#         elif apiKey == 'q' or apiKey == 'Q':
#             break
#         else:
#             error("Its not a valid API Key. To turn back press 'q'")


from message import success, error

def setApiKey():
    while True:
        apiKey = input("Introduce the API Key of Virus Total\n> ")
        if len(apiKey) > 10:
            write = False
            with open("conf.py", 'r') as file:
                lines = file.readlines()
            with open("conf.py", 'w') as file:
                for line in lines:
                    if line.startswith('vt_api_key='):
                        file.write("vt_api_key='{}'\n".format(apiKey))
                        write = True
                    else:
                        file.write(line)
                if not write:
                    file.write("vt_api_key='{}'\n".format(apiKey))
            success('Done!')
            break
        elif apiKey.lower() == 'q':
            break
        else:
            error("It's not a valid API Key. To turn back, press 'q'")
