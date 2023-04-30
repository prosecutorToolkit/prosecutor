# from datetime import datetime
# from sqlite3 import Timestamp
# from folium.plugins import plugins
# from folium import plugins

from pickle import FALSE
import time as t
from xmlrpc.client import TRANSPORT_ERROR
import pandas as pd, os, re, colorama, sys
from folium.plugins import FloatImage
from folium.plugins import HeatMap
import folium as folio

target_phone = False
target_ip = False
target_id_celda = False
target_num_celda = False
target_imei = False
target_imsi = False
target_localidad = False
target_provincia = False
sys.path.append('../helpers')
from helpers.launchFile import launchFile
for slash1 in "\\": slash = slash1

def create_map(match_path, map_path):
    global type_of_map, senializacion
    import datetime
    data = pd.read_csv(match_path, encoding='cp1252')
    data = data[['Orden cronologico', 'Fecha y hora', 'Id celda', 'Latitud', 'Longitud', 'Radio', 'Telefono con el que contacto', 'IP asignada', 'Duracion', 'IMEI del usuario', 'IMSI del usuario', 'Tipo (Entrante/Saliente)', 'Direccion celda', 'Provincia celda', 'Localidad celda', 'Numero celda']]
    map = folio.Map(location=[data.Latitud.mean(), data.Longitud.mean()], zoom_start=14, control_scale=True)
    if type_of_map == 2:

            # TERMINAR LUEGO: 
                # Chequear que este codigo para el mapa de calor funciona en otro archivo "prueba.py"
                # si no logro hacerlo funcionar, quitar la funcion que define la variable type_of_map
                # si logro hacerlo funcionar, debería agregar a cuando creo el archivo CSV base del mapa,
                # un conteo de cantidad de impactos por antena para luego con esta en esta función
                # indicar la cantidad por celda

        # for index, location_info in data.iterrows():
        #     id_celda = str(location_info["Id celda"])
        #     latitud = str(location_info["Latitud"])
        #     longitud = str(location_info["Longitud"])
        #     cantidad = str(location_info["Cantidad"])
        heat_data = [[row['Latitud'],row['Longitud']] for index, row in data.iterrows()]
        HeatMap(heat_data).add_to(map)
        folio.plugins.HeatMap(heat_data).add_to(map)
    else:
        points = list()
        for index, location_info in data.iterrows():
            order = str(location_info["Orden cronologico"])
            fecha_y_hora = str(location_info["Fecha y hora"])
            id_celda = str(location_info["Id celda"])
            radio = location_info["Radio"]
            tel = ""
            tel = str(location_info["Telefono con el que contacto"])
            ip = ""
            ip = str(location_info['IP asignada'])
            try: tipo = location_info['Tipo (Entrante/Saliente)']
            except: tipo = False
            tel_ip = ""
            if tipo == 'Entrante' or tipo == 'Saliente':
                tel_ip = "Clase: Llamada - Tel contactado: %s, Tipo: %s" %(tel, tipo)
            else: tel_ip = "Clase: Datos - IP asignada: %s" %ip
            duracion = str(location_info['Duracion'])
            latitud = location_info["Latitud"]
            longitud = location_info["Longitud"]
            # LUEGO AGREGAR DATOS DE LAS TITULARIDADES Y AGREGAR ACA CON EL NOMBRE DE LA PERSONA
            prov = str(location_info['Provincia celda'])
            loc = str(location_info['Localidad celda'])
            datos = "ORDEN: %s - Fecha y hora: %s - Radio: %s - %s - Duracion: %s - CELDA: %s - Localidad: %s - Provincia: %s" % (order, fecha_y_hora, str(radio), tel_ip, duracion, id_celda, loc, prov)
            folio.Marker([latitud, longitud], popup=datos).add_to(map)
            radio = radio *1000
            if senializacion == 1 or senializacion == 2:
                folio.Circle([latitud,longitud],radius=radio, fill_color='red').add_to(map)
            else: 
                folio.Circle([latitud,longitud], fill_color='red').add_to(map)
            points.append(tuple([latitud, longitud]))
        if senializacion == 1 or senializacion == 3:
            folio.PolyLine(points, color="red", weight=2.5, repeat=10, opacity=1, polygon=False, stroke=True).add_to(map)
        try:
            picture = os.path.dirname(__file__) + "\Logo_MPF.png"
            FloatImage(picture, bottom=3, left=3).add_to(map)
        except: "\nERROR: Cant found Logo_MPF.png"
        map.save(map_path)

def obtener_valores_fecha(fecha, hour):
    primer_valor = re.findall('^[0-9]*[^/]', fecha)
    primer_valor = primer_valor[0]
    medio_valor = re.findall('/[0-9]+/', fecha)
    medio_valor = medio_valor[0]
    medio_valor = medio_valor[1:-1]
    ultimo_valor = re.findall('[^/]*[0-9]$', fecha)
    ultimo_valor = ultimo_valor[0]
    hora = re.findall('^[0-9]*[^:]', hour)
    hora = hora[0]
    minuto = re.findall(':[0-9]+:', hour)
    minuto = minuto[0]
    minuto = minuto[1:-1]
    segundo = re.findall('[^:]*[0-9]$', hour)
    segundo = segundo[0]
    return primer_valor, medio_valor, ultimo_valor, hora, minuto, segundo

def get_time_stamp(fecha, hour, tipo):
    fecha = fecha.replace('-','/')

    primer_valor, medio_valor, ultimo_valor, hora, minuto, segundo = obtener_valores_fecha(fecha, hour)

    if int(tipo) == 1:
        dia = primer_valor
        mes = medio_valor
        anio = ultimo_valor
    elif int(tipo) == 2:
        mes = primer_valor
        dia = medio_valor
        anio = ultimo_valor
    elif int(tipo) == 3:
        anio = primer_valor
        mes = medio_valor
        dia = ultimo_valor

    from datetime import datetime
    dtime = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
    dtimestamp = dtime.timestamp()
    return int(round(dtimestamp))

__number__ = 0
__num_of_finished__ = 0
lista_de_fallas = list()
lista = list()
def create_dictionary(path, calls_path_date_format, calls_or_data, timestamp_inicio, timestamp_final):
    global __number__, __num_of_finished__
    global lista, lista_de_fallas
    data = pd.read_csv(path, encoding='cp1252')
    falla_num = 0
    if calls_or_data == "Calls":
        data = data[["Fecha", "Hora", "Celda Id", "IMEI", "IMSI", "Otro", "Durac", "Tipo" ,"Celda direccion", "Celda Num", "Celda localidad", "Celda provincia"]]
    elif calls_or_data == "Data":
        data = data[["Fecha", "Hora", "Celda Id", "IMEI", "IMSI", "IP Asig.", "DURACION (HH:MM:SS)", "Celda direccion", "Cel.Num", "Celda localidad", "Celda provincia"]]
    for index, location_info in data.iterrows():
        __number__ +=1
        try:
            fecha = str(location_info["Fecha"])
            try:
                fecha = fecha.split()
                fecha = fecha[0]
            except: fecha = "None"
            hora = str(location_info["Hora"])
            try:
                hora = hora.split()
                hora = hora[0]
            except: hora = "None"
            celda_id = str(location_info["Celda Id"])
            try:
                celda_id = celda_id.split()
                celda_id = celda_id[0]
            except: celda_id = "None"

            time_stamp = get_time_stamp(fecha, hora, calls_path_date_format)

            # CONTROL DE FECHA EN CASO DE QUE SE HAYA UTILIZADO
            if timestamp_inicio != False:
                if int(time_stamp) > timestamp_final or int(time_stamp) < timestamp_inicio: continue

            # CONTINUA RECOLECTANDO DATOS
            imei = str(location_info["IMEI"])
            try:
                imei = imei.split()
                imei = imei[0]
            except: imei = ""
            imsi = str(location_info["IMSI"])
            try:
                imsi = imsi.split()
                imsi = imsi[0]
            except: imsi = ""
            celda_direccion = str(location_info["Celda direccion"])
            celda_direccion = celda_direccion.replace(",", "")
            try:
                celda_direccion1 = celda_direccion.split()
                celda_direccion = ""
                for value in celda_direccion1: celda_direccion += value + " "
                celda_direccion = celda_direccion[:-1]
            except: celda_direccion = ""
            cel_pcia = str(location_info["Celda provincia"])
            try:
                cel_pcia1 = cel_pcia.split()
                cel_pcia = ""
                for value in cel_pcia1: cel_pcia += value + " "
                cel_pcia = cel_pcia[:-1]
            except: cel_pcia = ""
            cel_localidad = str(location_info["Celda localidad"])
            try:
                cel_localidad1 = cel_localidad.split()
                cel_localidad1 = ""
                for value in cel_localidad1: cel_localidad += value + " "
            except: cel_localidad = ""
            # ----------- DIFERENTE NOMBRE DEL DATO -------------
            try:
                try:
                    duracion = str(location_info["Durac"])
                    duracion = duracion.split()
                    duracion = duracion[0]
                except:
                    duracion = str(location_info["DURACION (HH:MM:SS)"])
                    duracion = duracion.split()
                    duracion = duracion[0]
            except: duracion = ""
            try:
                try:
                    cel_num = str(location_info["Celda Num"])
                    cel_num = cel_num.split()
                    cel_num = cel_num[0]
                except:
                    cel_num = str(location_info["Cel.Num"])
                    cel_num = cel_num.split()
                    cel_num = cel_num[0]
            except: cel_num = ""
            # --------------------- DIFIEREN --------------------
            try:
                tipo = str(location_info["Tipo"])
                tipo = tipo.split()
                tipo = tipo[0]
                if tipo == "E" or tipo == "e" or tipo == "entrante": tipo = "Entrante"
                elif tipo == "S" or tipo == "s" or tipo == "saliente": tipo = "Saliente"
            except: tipo = ""
            try:
                otro = str(location_info["Otro"])        # CORRESPONDE AL NUMERO TELEFICO CON EL QUE SE COMUNICO
                otro = otro.split()
                otro = otro[0]
            except: otro = ""
            try:
                ip = str(location_info["IP Asig."])      # PARA EL CASO DE LAS PLANILLAS DE DATOS CORRESPONDE LA IP ASIGNADA POR LA CNIA.
                ip = ip.split()
                ip = ip[0]
            except: ip = ""
            __num_of_finished__ +=1
            # ------------------------------------------------------
            # FILTROS
            global target_phone, target_ip, target_id_celda, target_num_celda, target_imei, target_imsi, target_localidad, target_provincia
            if target_phone != False and str(target_phone) != otro: continue
            if target_ip != False and str(target_ip) != ip: continue
            if target_id_celda != False and str(target_id_celda) != celda_id: continue
            if target_num_celda != False and str(target_num_celda) != cel_num: continue
            if target_imei != False and str(target_imei) != imei: continue
            if target_imsi != False and str(target_imsi) != imsi: continue
            if target_localidad != False and str(target_localidad) != cel_localidad: continue
            if target_provincia != False and str(target_provincia) != cel_pcia: continue

            # ------------------------------------------------------
            newtupple = (time_stamp, otro, ip, celda_id, duracion, imei, imsi, tipo, celda_direccion, cel_pcia, cel_localidad, cel_num)
            lista.append(newtupple)

        except:
            falla_num +=1
            valores_de_falla = "\n" + str(falla_num) + " in %s file:" % calls_or_data
            try: valores_de_falla+="\n    Fecha: "+str(fecha)
            except: pass
            try: valores_de_falla+="\n    Hora: "+str(hora)
            except: pass
            try: valores_de_falla+="\n    Timestamp: "+str(time_stamp)
            except: pass
            try: valores_de_falla+="\n    Celda ID: "+str(celda_id)
            except: pass
            try: valores_de_falla+="\n    Numero telefono contactado (otro): "+str(otro)
            except: pass
            try: valores_de_falla+="\n    IP: "+str(ip)
            except: pass
            try: valores_de_falla+="\n    Duración: "+str(duracion)
            except: pass
            try: valores_de_falla+="\n    IMEI: "+str(imei)
            except: pass
            try: valores_de_falla+="\n    IMSI: "+str(imsi)
            except: pass
            try: valores_de_falla+="\n    Tipo: "+str(tipo)
            except: pass
            try: valores_de_falla+="\n    Celda dirección: "+str(celda_direccion)
            except: pass
            try: valores_de_falla+="\n    Celda provincia: "+str(cel_pcia)
            except: pass
            try: valores_de_falla+="\n    Celda localidad: "+str(cel_localidad)
            except: pass
            try: valores_de_falla+="\n    Celda numero: "+str(cel_num)
            except: pass
            lista_de_fallas.append((valores_de_falla))
            valores_de_falla = ""


cells_dictionary = dict()
def antenas_to_dictionary(path):
    global cells_dictionary
    data = pd.read_csv(path, encoding='cp1252')
    data = data[["Cell", "Latitud", "Longitud", "Radio Cobertura en KM o Metros"]]
    for index, location_info in data.iterrows():
        celda = location_info["Cell"]
        celda = celda.split()
        celda = celda[0]
        latitud = location_info["Latitud"]
        try:
            latitud = latitud.replace(",.", ",").replace(".,", ",")
            latitud = float(latitud.replace(",", "."))
        except: pass
        longitud = location_info["Longitud"]
        try:
            longitud = longitud.replace(",.", ",").replace(".,", ",")
            longitud = float(longitud.replace(",", "."))
        except: pass
        radio = location_info["Radio Cobertura en KM o Metros"]
        try:
            radio = radio.replace(",.", ",").replace(".,", ",")
            radio = float(radio.replace(",", "."))
        except: pass
        cells_dictionary[celda] = (latitud, longitud, radio)

def excel_to_csv(path):
    if path.endswith('.xls'): new_name = path.replace('.xls', '.csv')
    elif path.endswith('.xlsx'): new_name = path.replace('.xlsx', '.csv')
    else: return "\nERROR, no ha indicado archivos en formato '.xls' o '.xlsx'"
    read_file = pd.read_excel (path)
    # print(type(read_file))
    # print("_________________________________________________\n_________________________________________________\n_________________________________________________\nREAD FILE\n_________________________________________________", read_file)
    read_file.to_csv(new_name, index = None, header=True)
    return new_name

def match(match_path):
    import datetime
    global lista
    lap=0
    import csv
    with open(match_path, 'w', newline='') as file:
        writer = csv.writer(file)
               # lap, time_stamp, celda_id, latitud, longitud, radio, otro, ip, duracion, imei, imsi, tipo, celda_direccion, cel_pcia, cel_localidad, cel_num
        row = [['Orden cronologico', 'Fecha y hora', 'Id celda', 'Latitud', 'Longitud', 'Radio', 'Telefono con el que contacto', 'IP asignada', 'Duracion', 'IMEI del usuario', 'IMSI del usuario', 'Tipo (Entrante/Saliente)', 'Direccion celda', 'Provincia celda', 'Localidad celda', 'Numero celda']]
        writer.writerows(row)
        for value in lista:
            try:
                time_stamp = value[0]
                time = str(datetime.datetime.fromtimestamp(time_stamp))
                otro = value[1]
                ip = value[2]
                celda_id = value[3]
                duracion = value[4]
                imei = value[5]
                imsi = value[6]
                tipo = value[7]
                celda_direccion = value[8]
                cel_pcia = value[9]
                cel_localidad = value[10]
                cel_num = value[11]

                data = cells_dictionary.get(celda_id)
                latitud = data[0]
                longitud = data[1]
                radio = data[2]

                lap +=1

                row = [[lap, time, celda_id, latitud, longitud, radio, otro, ip, duracion, imei, imsi, tipo, celda_direccion, cel_pcia, cel_localidad, cel_num]]
                writer.writerows(row)
            except: pass

def definir_formato(path):
    data = pd.read_csv(path, encoding='cp1252')
    data = data[["Fecha"]]
    fechas = ""
    for index, fecha_1 in data.iterrows():
        fecha = fecha_1["Fecha"]
        fechas += "--- " + fecha + "\n"
        if index == 5: break
    question = True
    while True:
        if question == True:
            texto = '''\n--- ¿Qué formato tienen estas fechas?
            \n1. Día/Mes/Año
            \n2. Mes/Día/Año
            \n3. Año/Mes/Día
            \n''' + fechas + "  > "
        else: texto = "  > "
        try: respuesta = int(input(texto))
        except:
            print("\nERROR, debe introducir un número!")
            continue
        if respuesta == 1 or respuesta == 2 or respuesta == 3:
            while True:
                try: valor = int(input("\n--- Está seguro?\n1. Sí\n2. No\n  > "))
                except: print("\nERROR, debe introducir un número!")
                if valor == 1 or valor == 2: break
        try:
            if valor == 1: break
        except: print("\nERROR, introduzca una ubicación válida")
        question == False
    return respuesta

def formato_input(tipo, primer_valor, medio_valor, ultimo_valor):
    if int(tipo) == 1:
        dia = primer_valor
        mes = medio_valor
        anio = ultimo_valor
    elif int(tipo) == 2:
        mes = primer_valor
        dia = medio_valor
        anio = ultimo_valor
    elif int(tipo) == 3:
        anio = primer_valor
        mes = medio_valor
        dia = ultimo_valor
    return dia, mes, anio

def validacion_y_timestamp(desde_hasta):
        import datetime
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = int(date.strftime("%Y"))
        while True:
            pregunta = "\n--- Defina un formato para la fecha '%s'\n1. DD/MM/AAAA\n2. MM/DD/AAAA\n3. AAAA/MM/DD\n  > " %desde_hasta
            tipo = input(pregunta)
            question = False
            if tipo == "1" or tipo == "2" or tipo == "3":
                fecha = input("--- %s:\n        Fecha:\n  > " % desde_hasta)
                hora = input("\n        Hora (HH:MM:SS):\n  > ")
                fecha = fecha.replace(":", "/").replace(".", "/").replace(",", "/").replace(";", "/").replace(slash, "/")
                hora = hora.replace("/", ":").replace(".", ":").replace(",", ":").replace(";", ":").replace(slash, ":")
                try:
                    format_validator = fecha.split("/")
                    for value in format_validator: x = int(value)
                except:
                    print("\nERROR, debe introducir números en la fecha, separados por /")
                    continue
                try:
                    format_validator = hora.split(":")
                    for value in format_validator: x = int(value)
                except:
                    print("\nERROR, debe introducir números en la hora, separados por :")
                    continue
                primer_valor, medio_valor, ultimo_valor, hour, minuto, segundo = obtener_valores_fecha(fecha, hora)
                dia, mes, anio = formato_input(tipo, primer_valor, medio_valor, ultimo_valor)
                if len(dia) > 2 or len(dia) < 1:
                    print("\nERROR, en la cantidad de dígitos del día"); continue
                try:
                    if int(dia) > 31: print("\nERROR, día incorrecto"); continue
                except: print("\nERROR, en el día no ha introducido un número"); continue
                if len(mes) > 2 or len(dia) < 1:
                    print("\nERROR, en la cantidad de dígitos del mes"); continue
                try:
                    if int(mes) > 12: print("\nERROR, mes incorrecto"); continue
                except: print("\nERROR, en el mes no ha introducido un número"); continue
                if len(anio) != 4:
                    print("\nERROR, en la cantidad de dígitos del año"); continue
                try:
                     if int(anio) > year: print("\nERROR, año incorrecto"); continue
                except: print("\nERROR, en el año no ha introducido un número"); continue
                try:
                      if int(hour) > 24 or int(hour) < 0: print("\nERROR, horas incorrectas"); continue
                except: print("\nERROR, en la hora no ha introducido un número"); continue
                try:
                       if int(minuto) > 59 or int(minuto) < 0: print("\nERROR, minutos incorrectos"); continue
                except: print("\nERROR, en el minuto no ha introducido un número"); continue
                try:
                        if int(segundo) > 59 or int(segundo) < 0: print("\nERROR, segundos incorrectos"); continue
                except: print("\nERROR, en los segundos no ha introducido un número"); continue
                answer = input('''\nConfirmar la siguiente fecha y hora '%s'?
                \nDIA: %s, MES: %s, AÑO: %s, HORA: %s, MINUTO: %s, SEGUNDO: %s
                \n\n1. Yes\n2. No\n  > ''' % (desde_hasta, dia, mes, anio, hour, minuto, segundo))
                if answer == "1" or answer == "y" or answer == "yes" or answer == "Yes": break
            else: print("\nERROR con el valor introducido")
        try:
            time_stamp_final = get_time_stamp(fecha, hora, tipo)
            return time_stamp_final
        except:
            print("\nERROR DESCONOCIDO")

def function_senialization():
    global type_of_map, senializacion
    first_type_of_map = True
    while True:
        if first_type_of_map == True:
            string = '''\n--- Qué tipo de mapa desea generar?
            \n1. Marcar de puntos de celdas impactadas y/o líneas cronológicamente y/o de radio de cobertura
            \n2. Mapa de calor
            \n  > '''
        else: string = "ERROR, debe introducir un número entre 1 y 2\n  > "
        try: type_of_map = int(input(string))
        except: type_of_map = False
        if type_of_map == 1 or type_of_map == 2: break
        first_type_of_map = False
        
    if type_of_map == 1:
        first_senializacion = True
        while True:
            if first_senializacion == True:
                string = '''\n--- Qué tipo de señalización desea en el mapa, además de la ubicación de las celdas impactadas?
                \n1. Marcar líneas cronológicamente y radio de cobertura de las celdas impactadas
                \n2. Marcar radio de cobertura de las celdas impactadas
                \n3. Marcar líneas cronológicamente
                \n4. Sólo marcar la ubicación de las celdas impactadas
                \n  > '''
            else: string = "ERROR, debe introducir un número del 1 al 4\n  > "
            try: senializacion = int(input(string))
            except: senializacion = False
            if senializacion == 1 or senializacion == 2 or senializacion == 3 or senializacion == 4: break
            first_senializacion = False


def __init__():
    x = 0
    import re
    start = True
    while start == True:
        print("\n____________________________________________________________________________________________________________________\n")
        try:
            question_1 = int(input('''
            \nQué desea realizar?
            \n1. Crear un reporte CSV y un mapa
            \n2. Crear un reporte CSV
            \n3. Crear un mapa según un reporte CSV
            \n4. Ayuda
            \n5. Cerrar
            \n  > '''))
            if question_1 < 1 or question_1 > 5: question_1 = int("falla")
        except: print("\nERROR, debe introducir un número válido entre las opciones"); continue
        if question_1 == 5: break
        if question_1 == 4:
            valor = ""
            print('''
            \n\nEste programa puede crear mapas e informes de Excel, basados en planillas de impactos de celdas telefónicas (datos y llamadas).
            \n\nUd. debe contar con los siguientes archivos en formato .xsl o .xslx remitidos por una empresa telefónica, con las columnas que se indicadas en cada caso:
            \n\n--  > Archivo con detalle de las celdas
            \n-- Cell
            \n-- Latitud
            \n-- Longitud
            \n-- Radio Cobertura en KM o Metros
            \n-----> Archivo de los impactos de Llamadas:
            \n-- Fecha
            \n-- Hora
            \n-- Celda Id
            \n-- IMEI
            \n-- IMSI
            \n-- Otro
            \n-- Durac
            \n-- Tipo
            \n-- Celda direccion
            \n-- Celda Num
            \n-- Celda localidad
            \n-- Celda provincia
            \n-----> Archivo de impactos de Datos móviles
            \n-- Fecha
            \n-- Hora
            \n-- Celda Id
            \n-- IMEI
            \n-- IMSI
            \n-- IP Asig.
            \n-- DURACION (HH:MM:SS)
            \n-- Celda direccion
            \n-- Cel.Num
            \n-- Celda localidad
            \n-- Celda provincia''')
            print("\nEs necesario contar con el archivo con detalle de celdas y por lo menos un archivo de impactos de datos o de llamadas.")
            print("\nLas primer fila debe indicar el nombre de las columnas, por lo que si hay otras filas -antes de los nombres de columnas- debe eliminarlas.")
            print("\nEl archivo con informe de celdas debe estar todo en una misma hoja, es decir que si la telefónica informó los datos de las celdas de llamadas y de datos en diferentes hojas del archivo de excel, debería unificarlas manualmente.")
            while True:
                valor = input('''
                \nPresione 'enter' para volver a inicio
                \nPresione 1 para cerrar
                \n  > ''')
                if valor == "" or valor == '1': break
            if valor == '1': break
            continue
        report_path = ""
        finish = ""
        if question_1 == 3:
            primera_vez = True
            finish = False
            while True:
                if primera_vez == True: string = "\n--- Elegir la carpeta del reporte CSV:\n  > "
                else: string = "\n  > "
                report_path = input(string)
                if report_path == "1": break
                if report_path.endswith(".csv") == False:
                    print(colorama.Fore.RED + "\nERROR, no ha seleccionado un archivo CSV\n1: Volver\n2. Cerrar");
                    print(colorama.Style.RESET_ALL)
                    continue
                function_senialization()
                fecha_actual = datetime.today().strftime('%Y-%m-%d - %H-%M')
                map_path = os.path.dirname(report_path)  + "\Map - %s.html" % fecha_actual
                try:
                    create_map(report_path, map_path)
                    print(colorama.Fore.BLUE + "\n--- Mapa creado creado con éxito!")
                    launch = ""
                    print(colorama.Fore.GREEN + "\n--- Do you want to launch the map?")
                    print(colorama.Style.RESET_ALL)
                    launch = input('''
                    \n1. Yes
                    \n2. No
                    \n  > ''')
                    if str(launch) == '1' or launch == "y" or launch == "Y" or launch == "Yes" or launch == "yes":
                        os.startfile(map_path)
                        print(colorama.Fore.GREEN + "\n--- The map is in the same folder as you excel files!")
                        print(colorama.Style.RESET_ALL)
                        finish = True
                        break
                except:
                    print(colorama.Fore.RED + '''\nERROR, el mapa no ha podido crearse.
                        \nAsegúrese de que el nombre de las columnas sean idénticas a las del reporte original y que no se hayan introducido comas (,) por error''')
                    print(colorama.Style.RESET_ALL)
        if finish == True: continue
        if report_path == "1": continue
        if report_path == "2": break
        if question_1 == 1 or question_1 == 2:
            calls_path_date_format = ""
            while True:
                antenas_path = input("\n--- Indicar la dirección del archivo de Celdas:\n**Por ejemplo: C:\\Users\\admin\\Desktop\\Celdas.xls\n--> ")
                if len(antenas_path) > 10 and (antenas_path.endswith('.xls') or antenas_path.endswith('.xlsx')): break
                print(colorama.Fore.RED +"\nERROR, introduzca una ubicación válida")
                print(colorama.Style.RESET_ALL)
            calls_path = ""
            # while True:
            while True:
                calls_path = input('''
                \n--- Indicar la carpeta del archivo de Llamadas:
                \n**Por ejemplo: C:\\Users\\admin\\Desktop\\Llamadas.xls
                \n**Introduzca 1 si NO CUENTA CON estos datos:
                \n  > ''')
                if calls_path == "1": break
                if len(calls_path) > 10 and (calls_path.endswith('.xls') or calls_path.endswith('.xlsx')): break
                print(colorama.Fore.RED + "\nERROR, introduzca una ubicación válida")
                print(colorama.Style.RESET_ALL)
                if calls_path == "1": break
            data_path = ""
            while True:
                if calls_path == "1": string = "\n--- Indicar la carpeta del archivo de Datos Móviles:\n--> "
                else: string = '''
                \n--- Indicar la carpeta del archivo de Datos Móviles:
                \n**Por ejemplo: C:\\Users\\admin\\Desktop\\Datos.xls
                \n**Introduzca 1 si NO CUENTA CON estos datos:
                \n--> '''
                data_path = input(string)
                if data_path == "1" and calls_path == "1":
                    print(colorama.Fore.RED + "\nERROR, no ha definido ninguna fuente de datos")
                    print(colorama.Style.RESET_ALL)
                    break
                if data_path == "1": break
                if len(data_path) > 10 and (data_path.endswith('.xls') or data_path.endswith('.xlsx')): break
                print(colorama.Fore.RED + "\nERROR, introduzca una ubicación válida")
                print(colorama.Style.RESET_ALL)
            if data_path == "1" and calls_path == "1": continue

            sin_primera_parte = False
            question = True
            dict_limits = dict()
            filtros = ""
            while True:
                timestamp_inicio = False
                timestamp_final = False
                target_phone = False
                target_ip = False
                target_id_celda = False
                target_num_celda = False
                target_imei = False
                target_imsi = False
                target_localidad = False
                target_provincia = False
                respuesta_confirmar = ""
                while True:
                    try:
                        # LIMITACIONES SELECCIONADAS
                        if sin_primera_parte == True:
                            pregunta = '''
                            \n2. Limitar por período de tiempo
                            \n3. Limitar por teléfono contactado
                            \n4. Limitar por IP asignada
                            \n5. Limitar por ID de celda
                            \n6. Limitar por número de celda
                            \n7. Limitar por IMEI del usuario
                            \n8. Limitar por IMSI del usuario
                            \n9. Limitar por localidad
                            \n10. Limitar por Provincia
                            \n  > '''
                        if question == True:
                            pregunta = '''
                            \n--- Desea aplicar filtros al informe?
                            \n1. No, generar el informe con todos los datos
                            \n2. Limitar por período de tiempo
                            \n3. Limitar por teléfono contactado
                            \n4. Limitar por IP asignada
                            \n5. Limitar por ID de celda
                            \n6. Limitar por número de celda
                            \n7. Limitar por IMEI del usuario
                            \n8. Limitar por IMSI del usuario
                            \n9. Limitar por localidad
                            \n10. Limitar por Provincia
                            \n  > '''
                        else: pregunta = "\n  > "
                        respuesta = str(input(pregunta))
                        if respuesta == '1' or respuesta == '2'or respuesta == '3'or respuesta == '4'or respuesta == '5'or respuesta == '6'or respuesta == '7'or respuesta == '8'or respuesta == '9'or respuesta == '10': break
                    except:
                        question = False
                        print(colorama.Fore.RED + "\nERROR, debe introducir un número entre 1 y 10")
                        print(colorama.Style.RESET_ALL)

                if respuesta == '1': break
                if respuesta == '2':
                    while True:
                        timestamp_inicio = validacion_y_timestamp("DESDE")
                        timestamp_final = validacion_y_timestamp("HASTA")
                        if timestamp_inicio > timestamp_final:
                            print(colorama.Fore.RED + "\nERROR, la fecha y hora de interes 'DESDE' es posterior a la fecha y hora 'HASTA'")
                            print(colorama.Style.RESET_ALL)
                            continue
                        if timestamp_inicio == timestamp_final:
                            print(colorama.Fore.RED +"\nERROR, la fecha y hora de interes 'DESDE' es idéntica a la fecha y hora 'HASTA'")
                            print(colorama.Style.RESET_ALL)
                            continue
                        import datetime
                        fecha_y_hora_inicio = str(datetime.datetime.fromtimestamp(timestamp_inicio))
                        fecha_y_hora_final = str(datetime.datetime.fromtimestamp(timestamp_final))
                        string="\n> Período de interés:\n          Desde: %s\n          Hasta: %s" %(fecha_y_hora_inicio, fecha_y_hora_final)
                        dict_limits.update({"periodo_de_interes": string})
                        break
                else:
                    timestamp_inicio = False
                    timestamp_final = False
                if respuesta == '3':
                    target_phone = str(input("\nIntroduzca el número de teléfono contactado objetivo\n  > "))
                    string = "\n> Teléfono contactado: %s" %target_phone
                    dict_limits.update({"target_phone": string})
                if respuesta == '4':
                    target_ip = str(input("\nIntroduzca la IP objetivo\n  > "))
                    string="\n> IP: %s" %target_ip
                    dict_limits.update({"target_ip": string})
                if respuesta == '5':
                    target_id_celda = str(input("\nIntroduzca la ID de Celda objetivo\n  > "))
                    string="\n> ID Celda: %s" %target_id_celda
                    dict_limits.update({"target_id_celda": string})
                if respuesta == '6':
                    target_num_celda = str(input("\nIntroduzca el número de Celda objetivo\n  > "))
                    string="\n> Número de Celda: %s" %target_num_celda
                    dict_limits.update({"target_num_celda": string})
                if respuesta == '7':
                    target_imei = str(input("\nIntroduzca el número IMEI objetivo\n  > "))
                    string="\n> IMEI: %s" %target_imei
                    dict_limits.update({"target_imei": string})
                if respuesta == '8':
                    target_imsi = str(input("\nIntroduzca el número IMSI objetivo\n  > "))
                    string="\n> IMSI: %s" %target_imsi
                    dict_limits.update({"target_imsi": string})
                if respuesta == '9':
                    target_localidad = str(input("\nIntroduzca la localidad objetivo\n  > "))
                    string="\n> Localidad: %s" %target_localidad
                    dict_limits.update({"target_localidad": string})
                if respuesta == '10':
                    target_provincia = str(input("\nIntroduzca la Provincia objetivo\n  > "))
                    string="\n> Provincia: %s" %target_provincia
                    dict_limits.update({"target_provincia": string})
                _first_ = True
                while True:
                    filtros = ""
                    for value in dict_limits.values(): filtros +=value
                    confirmar = '''\n--- Filtros aplicados:%s
                    \n--- Qué desea realizar?
                    \n1. Agregar o corregir un filtro
                    \n2. Confirmar filtros y continuar
                    \n3. Cancelar filtros y continuar
                    \n4. Cancelar filtros y volver a inicio
                    \n  > ''' % filtros
                    if _first_ == False:
                        confirmar = "\nERROR, debe elegir entre las opciones 1, 2, 3 o 4\n  > "
                    respuesta_confirmar = str(input(confirmar))
                    if respuesta_confirmar == '1' or respuesta_confirmar == '2' or respuesta_confirmar == '3' or respuesta_confirmar == '4': break
                    else: _first_ = False
                if respuesta_confirmar == '1': sin_primera_parte = True; continue
                elif respuesta_confirmar == '2': break
                elif respuesta_confirmar == '3' or respuesta_confirmar == '4':
                    dict_limits.clear()
                    timestamp_inicio = False
                    timestamp_final = False
                    target_phone = False
                    target_ip = False
                    target_id_celda = False
                    target_num_celda = False
                    target_imei = False
                    target_imsi = False
                    target_localidad = False
                    target_provincia = False
                    break
            if respuesta_confirmar == '4': continue

            print("\n--- Procesando datos...")

            antenas_path = excel_to_csv(antenas_path)
            if antenas_path == "\nERROR, no ha indicado archivos en formato '.xls' o '.xlsx'": continue # ESTO DEBERIA VALIDARSE ANTES AL INGRESAR LA DIRECCION
            print(colorama.Fore.GREEN + "\n--- CSV de celdas creado con éxito!")
            print(colorama.Style.RESET_ALL)

            if calls_path != "1":
                calls_path = excel_to_csv(calls_path)
                if calls_path == "\nERROR, no ha indicado archivos en formato '.xls' o '.xlsx'": continue
                print(colorama.Fore.GREEN +"\n--- CSV de llamadas creado con éxito!")
                print(colorama.Style.RESET_ALL)

            if data_path != "1":
                data_path = excel_to_csv(data_path)
                if data_path == "\nERROR, no ha indicado archivos en formato '.xls' o '.xlsx'": continue
                print(colorama.Fore.GREEN + "\n--- CSV de datos creado con éxito!")
                print(colorama.Style.RESET_ALL)

            try: antenas_to_dictionary(antenas_path)
            except: print('''\nERROR, ha confundido el Archivo de Celdas por otro archivo o éste no sigue los parámetros del programa
            \nEl archivo, en formato .xls o .xlsx, debe tener las siguientes columnas:
            \n'Cell', 'Latitud', 'Longitud', 'Radio Cobertura en KM o Metros' '''); continue
            print(colorama.Fore.GREEN +"\n--- Diccionario de celdas creado con éxito!")
            print(colorama.Style.RESET_ALL)

            calls_or_data = "Calls"

            if calls_path != "1":
                try:
                    print(calls_path, calls_or_data, timestamp_inicio, timestamp_final)
                    calls_path_date_format = definir_formato(calls_path)
                    print(calls_path_date_format)
                    create_dictionary(calls_path, calls_path_date_format, calls_or_data, timestamp_inicio, timestamp_final)
                    print(colorama.Fore.GREEN + "\n--- Diccionario de Llamadas creado con éxito!")
                    print(colorama.Style.RESET_ALL)
                except:
                    print(colorama.Fore.RED + '''\nERROR, ha confundido el Archivo de Llamadas por otro archivo o éste no sigue los parámetros del programa
                    \nEl archivo, en formato .xls o .xlsx, debe tener las siguientes columnas:
                    \n'Fecha', 'Hora', 'Celda Id', 'IMEI', 'IMSI', 'Otro', 'Durac', 'Tipo', 'Celda direccion', 'Celda Num', 'Celda localidad', 'Celda provincia' ''')
                    print(colorama.Style.RESET_ALL)
                    continue
            calls_or_data = "Data"
            if data_path != "1":
                try:
                    data_path_date_format = definir_formato(data_path)
                    create_dictionary(data_path, data_path_date_format, calls_or_data, timestamp_inicio, timestamp_final)
                    print(colorama.Fore.GREEN + "\n--- Diccionario de Datos Móviles creado con éxito!")
                except: print(colorama.Fore.RED + '''
                \nERROR, ha confundido el Archivo de Datos Móviles por otro archivo o éste no sigue los parámetros del programa
                \nEl archivo, en formato .xls o .xlsx, debe tener las siguientes columnas:
                \n'Fecha', 'Hora', 'Celda Id', 'IMEI', 'IMSI', 'IP Asig.', 'DURACION (HH:MM:SS)', 'Celda direccion', 'Cel.Num', 'Celda localidad', 'Celda provincia' '''); continue

            lista = sorted(lista, reverse = False)

            print(colorama.Fore.GREEN + "\n--- Cantidad de filas procesadas con éxito: %s / %s" % (__num_of_finished__, __number__))
            print(colorama.Style.RESET_ALL)

            fecha_actual = datetime.today().strftime('%Y-%m-%d - %H-%M')
            path = os.path.dirname(antenas_path)
            if len(lista_de_fallas) > 0:
                fails_path = path + '\Fallas - Ejecución %s.txt' % fecha_actual
                with open(fails_path, 'w') as f:
                    f.write("\n--- LISTA DE ERRORES EN LOS DATOS:")
                    for value in lista_de_fallas:
                        f.write(value)
                launch = input("\n--- Do you want to launch the fails file?\n1. Yes\n2. No\n  > ")
                if str(launch) == '1' or launch == "y" or launch == "Y" or launch == "Yes" or launch == "yes":
                    os.startfile(fails_path)
            else: print("\n--- No se encontraron errores en los datos")

            match_path = path + "\Report - %s.csv" % fecha_actual

            try:
                match(match_path)
                print(colorama.Fore.GREEN + "\n--- Cruce de celdas e impactos creado con éxito!")
            except: print("ERROR, al comparar datos"); continue

            if question_1 == 2:
                launch = input("\n--- Do you want to launch the CSV file?\n1. Yes\n2. No\n  > ")
                if str(launch) == '1' or launch == "y" or launch == "Y" or launch == "Yes" or launch == "yes":
                    os.startfile(match_path)
                    print("\n--- The CSV file is in the same folder as yours excels files!")
                continue
            
            function_senialization()

            map_path = path + "\Map - %s.html" % fecha_actual
            print("\n--- Creando el mapa, por favor espere...")
            # try:
            create_map(match_path, map_path)
            print(colorama.Fore.GREEN + "\n--- Mapa creado creado con éxito!")
            launch = ""
            launch = input(colorama.Fore.BLUE + "\n--- Do you want to launch the map?\n1. Yes\n2. No\n  > ")
            print(colorama.Style.RESET_ALL)
            if str(launch) == '1' or launch == "y" or launch == "Y" or launch == "Yes" or launch == "yes":
                launchFile(map_path)
                print("\n--- The map is in the same folder as you excel files")
            # except: print("\n--- ERROR, no se ha podido crear el mapa")

            launch = ""
            launch = input("\n--- Do you want to launch the CSV file?\n1. Yes\n2. No\n  > ")
            if str(launch) == '1' or launch == "y" or launch == "Y" or launch == "Yes" or launch == "yes":
                launchFile(match_path)
                print("\n--- The CSV is in the same folder as you excel files")

        first = True
        while True:
            if first == True:
                string = "\n--- Qué desea realizar?\n1. Volver al menú principal\n2. Cerrar\n  > "
            else: string = "\n  > "
            again = input(string)
            if str(again) == '1' or again == "Y" or again == "y" or again == "Yes" or again == "yes":
                start = True
                break
            elif str(again) == '2' or again == "N" or again == "n" or again == "No" or again == "no":
                start = False
                break
            first = False


if __name__ == "__main__":
    __init__()