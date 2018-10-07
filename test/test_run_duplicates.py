from unittest import TestCase
from unittest import mock
from solution.run_duplicates import main


class TestRun(TestCase):
    """
    Test functionality of main()
    """
    def test_wrong_input(self):
        """
        Test for ValueError if incorrect input
        """
        # Mock user input
        with mock.patch('builtins.input', return_value=r'./not_a_folder'):
            self.assertRaisesRegex(ValueError, main())

    def test_no_input(self):
        """
        Test for ValueError if no input
        """
        # Mock user input
        with mock.patch('builtins.input', return_value=''):
            self.assertRaisesRegex(ValueError, main())

    def test_right_input_correct_value(self):
        """
        Test return value. With the given set of files, the returned value should be ['4969']
        """
        # Mock user input
        # return_value = path from root folder to testing folder
        with mock.patch('builtins.input', return_value=r'../duplicate_files/test/files_for_testing/example_files'):
            self.assertEqual(['4969'], main())

