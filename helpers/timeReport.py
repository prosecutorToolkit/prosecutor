import time

def timeReport():
    hora_actual_utc = time.gmtime()  # Get the time at UTC format
    now = time.gmtime(time.mktime(hora_actual_utc) - 21600) # Convert to UTC-3 (Argentina). 21600 sec = 6 hours

    # Format "DD-MM-AAAA--HH-MM-SS"
    formattedDate = time.strftime("%d-%m-%Y", now)
    formattedHour = time.strftime("%H-%M-%S", now)
    formattedHandD = "--".join([formattedDate, formattedHour])

    return formattedHandD