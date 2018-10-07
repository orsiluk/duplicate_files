#!/usr/bin/env python3.7.0

from pathlib import Path
from os import path as os_path
from hashlib import sha256
import time
file_set = set()


def sha256_file(filename: os_path) -> str:
    """
    Calculate SHA256 for the current file.
    Read file in chunks, making sure it will work with larger files as well.

    :param filename: path to file that has to be encoded
    :returns: string representing the encoded file
    """
    h = sha256()
    # Open file with 'rb' - treat it as binary
    with open(filename, 'rb') as f:
        # Read file in 128 KiB chunks
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)

    return h.hexdigest()


def find_duplicates(path: Path)->[]:
    """
    Builds set of hashed files. If the entry already exists flag it as duplicate.

    :param path: path to the directory
    :returns: array of duplicate files
    """
    duplicates = []

    for current_file in path.iterdir():
        hashed_file = sha256_file(current_file)

        # Check if file in set if yes add name to array of duplicates else add to set.
        if hashed_file in file_set:
            duplicates.append(current_file.name)
        else:
            file_set.add(hashed_file)

    return duplicates


def main():

    directory = input('Path from current directory to folder we want to find the duplicates in.\n')
    try:
        if os_path.isdir(directory):
            # start_time = time.time()
            duplicates = find_duplicates(Path(directory))
            print(duplicates)
            # print(len(duplicates))
            # print("--- %s seconds ---" % (time.time() - start_time))
        else:
            raise ValueError
    except ValueError:
        print('You must provide a valid folder! \n')


if __name__ == '__main__':
    main()


