import abc
from hashlib import sha256
from pathlib import Path


class EncodeFile(object):
    """
    Define a general behaviour for a class that returns the binary of a given file.
    Implement default behavior for the interface common to all classes.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_encoding(self, path: Path) -> str:
        """
        Get encoding of a file given the path

        :param path: os.path
        :return a string containing the hashed value
        Dummy implementation for testing purposes
        """
        h = sha256()
        h.update(path.name)

        return h.hexdigest()
