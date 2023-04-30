import hashlib, os

# Este archivo funciona con Hash SHA-256
def merkleTree(directory):
    def get_hash(filename):
        """Obtiene el hash del archivo dado"""
        hash_sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    def get_dir_hash(directory):
        # Obtiene el hash del directorio dado (modo árbol de Merkle)
        if not os.path.exists(directory):
            return None

        if os.path.isfile(directory):
            return None

        # Si es un directorio, calcula el hash de los archivos y subdirectorios
        dir_hash = hashlib.sha256()

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = get_hash(file_path)
                dir_hash.update(file_hash.encode())

        return dir_hash.hexdigest()

    return get_dir_hash(directory)