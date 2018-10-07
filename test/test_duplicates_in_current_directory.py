from unittest import TestCase
from pathlib import Path

from solution.encode_file_sha256 import EncodeSha256
from solution.duplicates_in_current_directory import DuplicatesInCurrentDirectory
from solution.store_files_set import StoreFilesSet


class TestDuplicatesInCurrentDirectory(TestCase):
    """
    Test functionality of the DuplicatesInCurrentDirectory class
    """
    def setUp(self):
        self.duplicate_finder = DuplicatesInCurrentDirectory()
        self.encoding = EncodeSha256()
        self.unique_files = StoreFilesSet()

    def test_wrong_path(self):
        self.duplicate_finder.find_duplicates(Path(r'./not_existing_file'), self.encoding, self.unique_files)
        self.assertEqual([], self.duplicate_finder.get_duplicates())

    def test_no_path(self):
        self.duplicate_finder.find_duplicates(None, self.encoding, self.unique_files)
        self.assertEqual([], self.duplicate_finder.get_duplicates())

    def test_duplicates_empty_directory(self):
        path = Path(r'../duplicate_files/test/files_for_testing/empty_directory')
        self.duplicate_finder.find_duplicates(path, self.encoding, self.unique_files)
        self.assertEqual([], self.duplicate_finder.get_duplicates())

    def test_duplicates_correct_value(self):
        path = Path(r'../duplicate_files/test/files_for_testing/example_files')
        self.duplicate_finder.find_duplicates(path, self.encoding, self.unique_files)
        self.assertEqual(['4969'], self.duplicate_finder.get_duplicates())
