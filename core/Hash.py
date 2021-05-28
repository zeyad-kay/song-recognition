import imagehash
from PIL import Image

class Hash():
    @staticmethod
    def generate_hash_code(array) :
        arr = Image.fromarray(array)
        hash = imagehash.phash(arr,hash_size=16).__str__()
        return hash