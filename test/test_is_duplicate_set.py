from unittest import TestCase

from solution.store_files_set import StoreFilesSet


class TestEncodeSha256(TestCase):
    """
    Test functionality of the IsDuplicateSet class
    """
    def setUp(self):
        self.duplicates_set = StoreFilesSet()

    def test_empty_string(self):
        self.assertEqual(True, self.duplicates_set.add_item(''))

    def test_string_is_none(self):
        with self.assertRaises(ValueError):
            self.duplicates_set.add_item(None)

    def test_string_is_duplicate(self):
        self.duplicates_set.add_item('I am a string.')
        self.assertEqual(False, self.duplicates_set.add_item('I am a string.'))

    def test_string_is_not_duplicate(self):
        self.duplicates_set.add_item('I am a string.')
        self.assertEqual(True, self.duplicates_set.add_item('I am another string.'))
