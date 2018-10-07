import abc
from pathlib import Path
from solution.store_files import StoreFiles
from solution.encode_file import EncodeFile


class Duplicates(object):
    """
    Define a general behaviour for a class that returns the binary of a given file.
    Implement default behavior for the interface common to all classes.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def find_duplicates(self, path: Path, encoding: EncodeFile, duplicate_set: StoreFiles):
        """
        Builds array of names of duplicate files.

        :param path: path to the directory
        :param encoding: class to be used to perform encoding
        :param duplicate_set: class that stores the hashed values of the files

        """

        pass

    @abc.abstractmethod
    def get_duplicates(self):
        """
        :return: array of duplicate files
        """
        pass
