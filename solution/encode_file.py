import abc
from pathlib import Path


class EncodeFile(object):
    """
    Define a general behaviour for a class that returns the binary of a given file.
    Implement default behavior for the interface common to all classes.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_encoding(self, file_name: Path) -> str:
        """
        Get encoding of a file given the path

        :param file_name: os.path
        :return a string containing the hashed value
        """

        pass
