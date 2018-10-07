from hashlib import sha256
from solution.encode_file import EncodeFile
from pathlib import Path


class EncodeSha256(EncodeFile):
    """
    Return a sha256 encoded version of a file from the given path
    """

    def get_encoding(self, file_name: Path) -> str:
        """
        Calculate SHA256 for the current file.
        Read file in chunks, making sure it will work with larger files as well.
        :param file_name: path to file
        :return a sha256 encoded string
        """

        if file_name and not file_name.is_file():
            raise FileNotFoundError('This is not a valid file!')

        hash_func = sha256()
        # Open file with 'rb' - treat it as binary
        with open(file_name, 'rb') as f:
            # Read file in 128 KiB chunks
            for b in iter(lambda: f.read(128 * 1024), b''):
                hash_func.update(b)

        return hash_func.hexdigest()
