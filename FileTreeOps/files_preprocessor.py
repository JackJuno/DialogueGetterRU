import os
from chardet.universaldetector import UniversalDetector
from loguru import logger


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
        new_file_name = f"{str(counter)}.txt"
        destination_path = os.path.join(new_path, new_file_name)
        with open(destination_path, 'w', encoding='utf-8') as text:
            with open(filename, 'r', encoding=encodings_str) as f:
                for line in f:
                    text.writelines(line)
        counter += 1
