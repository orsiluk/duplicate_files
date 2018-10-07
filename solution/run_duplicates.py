#!/usr/bin/env python3.7.0

from pathlib import Path
from solution.store_files_set import StoreFilesSet
from solution.encode_file_sha256 import EncodeSha256
from solution.duplicates_in_current_directory import DuplicatesInCurrentDirectory


def main():
    my_directory = input('Please provide relative path to the target folder to look for duplicates.\n')
    try:
        if Path.is_dir(Path(my_directory)) and my_directory != '':
            file_encoding = EncodeSha256()
            duplicate_set = StoreFilesSet()
            duplicates_in_directory = DuplicatesInCurrentDirectory()
            duplicates_in_directory.find_duplicates(Path(my_directory), file_encoding, duplicate_set)
            return duplicates_in_directory.get_duplicates()
        else:
            raise ValueError("You must provide a valid folder!")
    except ValueError:
        return


if __name__ == '__main__':
    result = main()
    print(result)
