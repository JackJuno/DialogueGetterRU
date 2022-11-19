import os
import re
from chardet.universaldetector import UniversalDetector
from loguru import logger


def check_newlines_pattern(path_to_text: str) -> str:
    result: str = ''
    normal_lines_counter = 0
    abrupt_lines_counter = 0
    detector = UniversalDetector()
    # check file code page encoding
    with open(path_to_text, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        encoding_str = detector.result['encoding']
    # open file
    with open(path_to_text, 'r', encoding=encoding_str) as f:
        line = f.readline()
        while line:
            # count patterns
            if re.match("^(\s*)(-|—)(\s*)[А-Я]", line):
                if re.search("(\.|\!|\?)$", line):
                    normal_lines_counter += 1
                if re.search("[а-яА-Я0-9–-]$", line):
                    abrupt_lines_counter += 1
            line = f.readline()
    if normal_lines_counter > abrupt_lines_counter:
        result = 'normal'
    if normal_lines_counter < abrupt_lines_counter:
        result = 'abrupter'
    return result


def check_n_fix_newlines_pattern(texts_dir):
    # vars
    text_file_paths = []
    # create result filepath
    result_directory_name = "preprocessed_files"
    result_path = os.path.join(texts_dir, result_directory_name)
    try:
        os.makedirs(result_path, exist_ok=True)
        logger.info(f"Directory <{result_directory_name}> created successfully")
    except OSError as error:
        logger.error(f"Directory <{result_directory_name}> can not be created:\n{error}")
    # walk through the file tree
    for root, directories, files in os.walk(texts_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            text_file_paths.append(filepath)
    # loop through text files paths
    counter = 1
    for txt_file in text_file_paths:
        result_file_name = f"{str(counter)}.txt"
        result_file_path = os.path.join(result_path, result_file_name)
        tmp_str = []
        dialogue_flag = False
        detector = UniversalDetector()
        # check file code page encoding
        with open(txt_file, 'rb') as tf:
            for line in tf:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            encoding_str = detector.result['encoding']
            tf.close()
        with open(result_file_path, 'w', encoding='utf-8') as text:
            with open(txt_file, 'r', encoding=encoding_str) as f:
                pattern = check_newlines_pattern(txt_file)
                if pattern == 'normal':
                    for line in f:
                        text.write(line +"\n")
                if pattern == 'abrupter':
                    line = f.readline()
                    while line:
                        if re.match("(\s*)(-|—)(\s*)[А-Я]", line):
                            dialogue_flag = True
                            line.strip()
                            line = re.sub("\n", "", line)
                            tmp_str.append(line)
                        else:
                            if dialogue_flag:
                                line.strip()
                                line = re.sub("\n", "", line)
                                if re.search("[\.\!\?]\s*$", line):
                                    tmp_str.append(line)
                                    complete_sentence = ' '.join(tmp_str)
                                    text.write(complete_sentence + "\n\n")
                                    dialogue_flag = False
                                    tmp_str = []
                                else:
                                    tmp_str.append(line)
                            else:
                                text.write(line + '\n\n')
                        line = f.readline()
        counter+=1
