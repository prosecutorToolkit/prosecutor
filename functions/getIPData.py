import socket, geocoder, ssl, json, urllib, sys, os, pyperclip, folium, csv, tkinter as tk

sys.path.append('../helpers')
from helpers.launchFile import launchFile
from helpers.timeReport import timeReport
from helpers.yesNo import yesNo
from helpers.message import error, success, yellow
from helpers.askPath import askPath


def getIPData():

    def get_text():
        text = text_box.get("1.0", "end-1c")  # Obtiene el texto del cuadro de texto
        global s_text_url  # Guarda el texto en una variable global
        s_text_url = text
        root.destroy()  # Crea una ventana de tkinter

    root = tk.Tk()
    root.title("🔎 Introduce the URL or IP (one for line)  / Example: Google.com or 8.8.8.8")
    text_box = tk.Text(root)  # Crea un cuadro de texto
    text_box.pack()
    button = tk.Button(root, text="Save", command=get_text)  # Crea un botón para obtener el texto
    button.pack()
    root.mainloop()  # Inicia el loop principal de la ventana

    yellow('Ok. Working on it...')
    IPsURLslist = s_text_url.split('\n')
    point = False
    for digit in s_text_url:
        if digit == '.': point = True
    if len(s_text_url) < 4 or point == False:
        error('Please set a valid URL or IP');
        getIPData()
        
    def askAPI(text_url):
        global location
        ip = socket.gethostbyname(text_url)
        ip_1 = geocoder.ip(ip)
        location = ip_1.latlng
        url = 'http://ip-api.com/json/' + ip
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()
        data = data.decode()
        info = json.loads(data)
        lat = info['lat']
        lon = info['lon']
        country = info['country']
        country_code = info['countryCode']
        region = info['region']
        regionname = info['regionName']
        city = info['city']
        zip = info['zip']
        timezone = info['timezone']     
        isp = info['isp']
        org = info['org']
        a_as = info['as']
        values = [text_url,ip,isp,org,a_as,city,regionname,country,country_code,region,zip,str(lat),str(lon),timezone]
        return values

    def createCSV():
        try:
            directory = askPath()
            os.chdir(directory)
            destination_dir = os.getcwd()

            print("Working on it, please wait")
            ipPathCSV = os.path.join(destination_dir, 'Prosecutor - IPs data - ', f"{timeReport()}.csv")
            # ipPathCSV = destination_dir + '/Prosecutor - IPs data - ' + timeReport() + '.csv'

            with open(ipPathCSV, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(("SEARCH TERM","IP","ISP","ORG","AS","CITY","REGION NAME","COUNTRY"," COUNTRY CODE","REGION","ZIP CODE","LATITUDE","LONGITUDE","TIMEZONE"))
                for ip in IPsURLslist:
                    if len(ip) < 5:
                        pass
                    else:
                        try:
                            data = askAPI(ip)
                            writer.writerow(data)
                        except: pass
            success('CSV file with IPs data was created successfully!')
            launchFile(ipPathCSV)
        except:
            error("I'm sorry, probably you are not online and Prosecutor can't do this work within.")
    
    def IPWithMap(ipURL):
        # map_path = os.path.dirname(os.path.realpath(__file__)) + "/" + timeReport() + "map.html"

        global view_map_button, text_url
        try:
            values_1 = askAPI(ipURL)
            head = ["SEARCH TERM: ","\n\nDATA:\n  IP: ","\n  ISP: ","\n  Org: ","\n  As: ","\n  City: ","\n  Region name: ","\n  Country: ","\n  Country Code: ","\n  Region: ","\n  Zip code: ","\n  Latitude: ","\n  Longitude: ","\n  Timezone: "]
            x = 0
            values = ""
            for value in values_1:
                head_1 = head[x]
                values = values + head_1 + value
                x+=1
            pyperclip.copy(values)
            success("\nThe URL/IP data is in the clipboard!")
            yellow("\n" + values)
            confirm = yesNo('Do you want to launch the map 🌎? (y/n)\n  > ')
            if confirm:
                # AGREGAR PARA PREGUNTAR DONDE GUARDARLO
                map_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{timeReport()}map.html")
                map = folium.Map(location=location, zoom_start=10)
                folium.CircleMarker(location=location, radius=50, color="red").add_to(map), folium.Marker(location).add_to(map)
                map.save(map_path)
                launchFile(map_path)

        except: error("Probably you are not online and Prosecutor can't do this work within. If its not true, try again later and if it persist.")
    
    if len(IPsURLslist) == 0: print("x ERROR")
    elif len(IPsURLslist) == 1: IPWithMap(IPsURLslist[0])
    else: createCSV()