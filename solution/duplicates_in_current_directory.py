from pathlib import Path
from solution.store_files import StoreFiles
from solution.encode_file import EncodeFile
from solution.duplicates import Duplicates


class DuplicatesInCurrentDirectory(Duplicates):

    def __init__(self):
        self.duplicates = []

    def find_duplicates(self, path: Path, encoding: EncodeFile, unique_files: StoreFiles) -> []:
        """
        Builds set of hashed files retrieved from folder. If the entry already exists flag it as duplicate.

        :param path: path to the directory with NO subdirectories
        :param encoding: class to be used to perform encoding
        :param unique_files: class that stores the hashed values of the files
        """

        # Check if the given path is not None and is a directory
        if path and Path.is_dir(path):
            # Iterates over files in the directory
            for current_file in path.iterdir():

                # Doesn't check for subdirectories
                if current_file.is_file():
                    hashed_file = encoding.get_encoding(current_file)

                    # If couldn't be added to the set it's a duplicate
                    if unique_files.add_item(hashed_file) == False:
                        self.duplicates.append(current_file.name)

    def get_duplicates(self):
        """
        :return: array of duplicate files
        """
        return self.duplicates
