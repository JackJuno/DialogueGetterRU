import glob
import os
from chardet.universaldetector import UniversalDetector
from loguru import logger
from TextOps.text_preprocessor import *


def check_n_change_to_utf(src_file_paths, parent_dir_path):
    # create new directory in src dir
    new_directory_name = "automatically_created_copies_of_utf_encoded_files"
    # path to new dir
    new_path = os.path.join(parent_dir_path, new_directory_name)
    try:
        os.makedirs(new_path, exist_ok=True)
        logger.info(f"Directory <{new_directory_name}> created successfully")
    except OSError as error:
        logger.error(f"Directory <{new_directory_name}> can not be created:\n{error}")
    # check files code pages & save them with utf encodings
    detector = UniversalDetector()
    counter: int = 1
    for filename in src_file_paths:
        detector.reset()
        # encodings_str = ''
        with open(filename, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            encodings_str = detector.result['encoding']
            f.close()
        new_file_name = f"utf_src_{str(counter)}.txt"
        destination_path = os.path.join(new_path, new_file_name)
        with open(destination_path, 'w', encoding='utf-8') as text:
            with open(filename, 'r', encoding=encodings_str) as f:
                for line in f:
                    text.writelines(line)
        counter += 1
    # check text newline pattern & remove breaks in dialogue lines -> files ready for dialogues extraction
    check_n_fix_newlines_pattern(new_path)


def merge_files_in_directory(path):
    # make a list of files in the dataset output directory
    files_paths = [os.path.join(path, x) for x in os.listdir(path)]
    # create a path to all-in-one dataset file
    file_name = 'all_in_one_dataset_file.txt'
    new_file_path = os.path.join(path, file_name)
    # create all in one dataset file in add
    with open(new_file_path, mode='a', encoding='utf-8') as output_file:
        for pth in files_paths:
            try:
                with open(pth, mode='r', encoding='utf-8') as input_file:
                    output_file.write(input_file.read())
            except IOError:
                logger.error(f'Can not open file: {pth}')


def delete_files_except_one(path_to_dir, name_of_file_to_keep):
    file_to_keep_path = os.path.join(path_to_dir, name_of_file_to_keep)
    path_for_glob_search = os.path.join(path_to_dir, '*.*')
    # check if file to keep exists
    if os.path.isfile(file_to_keep_path):
        # then delete tmp files
        for file_name in glob.glob(path_for_glob_search):
            if not file_name.endswith(name_of_file_to_keep):
                os.remove(file_name)
    else:
        logger.info('You have not merged all datasets created in output directory into all-in-one big dataset file, so we keep all of them as they are.')

