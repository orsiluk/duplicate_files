import abc


class StoreFiles(object):
    """
    Decide if a file is a duplicate.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_item(self, string_to_add: str) -> bool:
        """
        :param string_to_add: string representing a file
        :return: boolean representing whether a file was added or already existed meaning it
        was a duplicate
        """
        pass
