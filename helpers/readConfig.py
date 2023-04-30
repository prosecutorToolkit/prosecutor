import setApiKey

def readConfig(value):
    # the reason of use this method inside a simple import thats
    # about allow change the apikey without close the program
    try:
        with open("conf.py", 'r') as file:
            content = file.read()
            lines = content.split('\n')
            for line in lines:
                if line.startswith(value):
                    _, valor = line.split('=')
                    returnValue = valor.strip().strip("'")
            if len(returnValue) < 10 & value != "auto_start": setApiKey()
    except:
        if value == "auto_start":
            returnValue = ""
        else:
            setApiKey()
            value1 = value  #chequear si python baja el valor automatico o hay que hacer esto pq funcione, parece q no por las lineas de arriba que llamo al mismo value en line.startswith(value)
            readConfig(value1)
    return returnValue