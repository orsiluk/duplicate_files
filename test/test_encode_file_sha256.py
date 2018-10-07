from unittest import TestCase
from solution.encode_file_sha256 import EncodeSha256
from pathlib import Path
from hashlib import sha256


class TestEncodeSha256(TestCase):
    """
    Test functionality of the EncodeSha256 class
    """

    def setUp(self):
        self.encoding = EncodeSha256()

    def test_wrong_path(self):
        with self.assertRaises(FileNotFoundError):
            self.encoding.get_encoding(Path(r'./not_existing_file'))

    def test_no_path(self):
        with self.assertRaises(TypeError):
            self.encoding.get_encoding(None)

    def test_encoding_empty_file(self):
        hash_func = sha256(b'')
        hash_val = hash_func.hexdigest()
        path = Path(r'../duplicate_files/test/files_for_testing/empty_file')
        self.assertEqual(hash_val, self.encoding.get_encoding(path))

    def test_encoding_accuracy(self):
        path = Path(r'../duplicate_files/test/files_for_testing/example_files/4969')
        hash_func = sha256()
        with open(path, 'rb') as f:
            file = f.read()
        hash_func.update(file)
        hash_val = hash_func.hexdigest()
        self.assertEqual(hash_val, self.encoding.get_encoding(path))

    def test_got_directory_instead_of_file(self):
        with self.assertRaises(FileNotFoundError):
            self.encoding.get_encoding(Path(r'../duplicate_files/test/files_for_testing/example_files'))



