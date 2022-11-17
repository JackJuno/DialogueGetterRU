import os
from FileTreeOps.files_preprocessor import *


def get_filepaths(dir_path: str) -> list:
    file_paths = []
    # walk through the file tree
    for root, directories, files in os.walk(dir_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def pipeline(src_dir_path):
    # open src dir & pre-process files -> list of files ready to change to utf-8
    src_filepaths_list = get_filepaths(src_dir_path)
    # check language, char code & change to utf-8 -> create a new dir with .txt files ready for str purification
    check_n_change_to_utf(src_filepaths_list, src_dir_path)
    # check str format pattern & remove breaks in dialogue lines -> files ready for dialogues extraction

# pipeline('/home/zonengeistbot/Documents/test') # /home/zonengeistbot/Documents/test
