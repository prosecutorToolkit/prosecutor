import hashlib, sys

sys.path.append('../helpers')
from helpers.message import error

def getsha256file(file):
    try:
        hashsha = hashlib.sha256()
        with open(file, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashsha.update(bloque)

        return hashsha.hexdigest()

    except:
        error('Unknown error hashing. ID=H2')
        return 'ERROR'