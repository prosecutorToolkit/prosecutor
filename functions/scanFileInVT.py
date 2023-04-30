import json
import sys, colorama, requests, hashlib
from anytree import Node, RenderTree

sys.path.append('../helpers')
from helpers.readConfig import readConfig
from helpers.selectFileFolder import selectFileFolder
from helpers.message import error

def scanFileInVT(file = False):
    try:
        if not file: file = selectFileFolder('File')
        
        # Ask the VirusTotal API
        vt_api_key = readConfig('vt_api_key')

        fh = open(file, "rb")
        data = fh.read()
        fh.close()

        sha256 = hashlib.sha256(data).hexdigest() # El hash del archivo que deseas buscar

        url = 'https://www.virustotal.com/vtapi/v2/file/report' # URL de la API de VirusTotal para la consulta de informacion del archivo
        params = {'apikey': vt_api_key, 'resource': sha256} # Parámetros de la solicitud
        response = requests.get(url, params=params) # Hacer la solicitud a la API de VirusTotal
        json_response = response.json()  # Analizar la respuesta JSON
        print('Hash of the file: ', json_response['resource']) # Imprimir la información del archivo

        # Crear el nodo raíz
        root = Node("SCAN")

        # Agregar nodos secundarios para cada escaneo
        try:
            for key in json_response['scans']:
                scanner = Node(key, parent=root)
                detected = Node("Detected: " + str(json_response['scans'][key]['detected']), parent=scanner)
                version = Node("Version: " + json_response['scans'][key]['version'], parent=scanner)
                result = Node("Result: " + str(json_response['scans'][key]['result']), parent=scanner)
                update = Node("Update: " + json_response['scans'][key]['update'], parent=scanner)

            # Imprimir el árbol
            for pre, fill, node in RenderTree(root):
                if node.name == "Detected: True":
                    print(colorama.Fore.RED + "%s%s" % (pre, node.name))
                elif node.name == "Detected: False":
                    print(colorama.Fore.GREEN + "%s%s" % (pre, node.name))
                else:
                    print(colorama.Fore.YELLOW + "%s%s" % (pre, node.name))
        except:
            error("The file is not at the Virus Total Database\nYou should upload the file manually: https://www.virustotal.com/gui/home/upload")
    except:
        error("Cant ask Virus Total API") 