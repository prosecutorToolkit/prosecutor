import sys, json, colorama

sys.path.append('../helpers')
from helpers.readConfig import readConfig
from helpers.message import red, error
from helpers.yesNo import yesNo
from helpers.setApiKey import setApiKey

def scanIPURLInVT():
    import virus_total_apis
    vt_api_key = readConfig('vt_api_key')
    ip_url = input("Introduce the URL or IP  / Example: Google.com  or  8.8.8.8\n  > ")
    point = False
    for digit in ip_url:
        if digit == '.': point = True
    try:
        if len(ip_url) < 4 or not point:
            red('Please set a valid URL or IP')
            scanIPURLInVT()
        switch_api_key = virus_total_apis.PublicApi(vt_api_key)
        response = switch_api_key.get_url_report(ip_url)
        raw_data_json = json.dumps(response, sort_keys=True, indent=4)
        # Convertir la respuesta de la API en un objeto JSON
        api_response_json = json.loads(raw_data_json)
        from anytree import Node, RenderTree
        # Crear el nodo raíz del árbol
        root = Node("API Response")
        # Añadir nodos hijos para los campos de la respuesta de la API
        Node(f"response_code: {api_response_json['response_code']}", parent=root)
        results_node = Node("results", parent=root)
        Node(f"filescan_id: {api_response_json['results']['filescan_id']}", parent=results_node)
        Node(f"permalink: {api_response_json['results']['permalink']}", parent=results_node)
        Node(f"positives: {api_response_json['results']['positives']}", parent=results_node)
        Node(f"resource: {api_response_json['results']['resource']}", parent=results_node)
        Node(f"response_code: {api_response_json['results']['response_code']}", parent=results_node)
        Node(f"scan_date: {api_response_json['results']['scan_date']}", parent=results_node)
        Node(f"scan_id: {api_response_json['results']['scan_id']}", parent=results_node)

        # Añadir un nodo hijo para el objeto "scans"
        scans_node = Node("scans", parent=results_node)

        # Añadir nodos hijos para cada escaneo en "scans"
        for scan_name, scan_data in api_response_json['results']['scans'].items():
            scan_node = Node(scan_name, parent=scans_node)
            Node(f"detected: {scan_data['detected']}", parent=scan_node)
            Node(f"result: {scan_data['result']}", parent=scan_node)

        print(colorama.Fore.YELLOW)
        if int(api_response_json['results']['positives']) > 0:
            print(colorama.Fore.MAGENTA)
        elif int(api_response_json['results']['positives']) > 5:
            print(colorama.Fore.RED)

        print('\n')
        # print the tree
        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")

    except:
        error("Could be an error in your API Key")
        while True:
            answer = yesNo("Do you want to set a new API Key? (y/n)")
            if answer:
                setApiKey()
            break