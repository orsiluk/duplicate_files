from solution.store_files import StoreFiles


class StoreFilesSet(StoreFiles):
    """
    Class checking if a file is already in the set, meaning it's a duplicate. If it is not,
    add it to the set.
    """
    def __init__(self):
        self.file_set = set()

    def add_item(self, string_to_add: str) -> bool:
        """
        Add item to the set.

        :param string_to_add: a string that should be added to the set
        :return: True if it was added successfully, otherwise False
        """
        if string_to_add is None:
            raise ValueError('"None" values not supported')

        if string_to_add in self.file_set:
            return False

        self.file_set.add(string_to_add)
        return True
