import sys, subprocess, re, os

from message import success, error

def docxToPdfUnix(file_path):
    try:
        def libreoffice_exec():
            # TODO
            if sys.platform == 'darwin':
                return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
            return 'libreoffice'

        args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', str(os.path.dirname(file_path)), file_path]
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Verificar el código de salida del proceso hijo
        if process.returncode != 0:
            print(process.stderr.decode())
        else:
            filename = re.search('-> (.*?) using filter', process.stdout.decode())
            if filename is None:
                error('Cant create PDF')
            else:
                success('PDF was created')
                # print("Archivo convertido con éxito: ", filename.group(1))

        return True

    except:
        return False

# docxToPdfUnix('/home/admin1/Desktop/abc.docx')