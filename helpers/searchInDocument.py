import zipfile, re, os

def search_in_document(filename, searchTerm):
    ext = os.path.splitext(filename)[1].lower()

    if ext == '.doc' or ext == '.docx' or ext == '.odt':
        # Abrir archivo y extraer contenido
        with zipfile.ZipFile(filename) as doc_zip:
            # Obtener una lista de nombres de archivo en el archivo zip
            file_list = doc_zip.namelist()

            # Buscar término de búsqueda en cada archivo
            for f_name in file_list:
                if f_name.endswith('.xml'):
                    with doc_zip.open(f_name) as f:
                        content = f.read().decode('utf-8')
                        if re.search(searchTerm, content):
                            return True, f_name
    elif filename.endswith('.doc'):
        # Abrir archivo y extraer contenido
        with open(filename, 'rb') as doc_file:
            content = doc_file.read()

        # Buscar término de búsqueda en el contenido
        if re.search(searchTerm, content.decode('utf-8', errors='ignore')):
            return True

    # El archivo no es de formato compatible o no se encontró el término de búsqueda
    return False

print(search_in_document('/home/admin1/Downloads/discurso.docx', 'RIMOLI'))