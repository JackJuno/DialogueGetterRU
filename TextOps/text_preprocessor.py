import os
import re
from chardet.universaldetector import UniversalDetector
from loguru import logger


def check_newlines_pattern(path_to_text: str) -> str:
    result: str = ''
    normal_lines_counter: int = 0
    abrupt_lines_counter: int = 0
    # # check file code page encoding
    # detector = UniversalDetector()
    # with open(path_to_text, 'rb') as f:
    #     for line in f:
    #         detector.feed(line)
    #         if detector.done:
    #             break
    #     detector.close()
    #     encoding_str = detector.result['encoding']
    # open file
    with open(path_to_text, 'r', encoding='utf-8') as f:  # utf-8 or encoding_str
        line = f.readline()
        while line:
            # count patterns
            if re.match(r"^\s*[-—]\s*[А-ЯA-Z0-9]", line):
                if re.search(r"[.!?]$", line):
                    normal_lines_counter += 1
                if re.search(r"[а-яА-Яa-zA-Z0-9–-]$", line):
                    abrupt_lines_counter += 1
            elif re.match(r"^\s*-\s*-\s*[А-ЯA-Z0-9]", line):
                if re.search(r"[.!?]$", line):
                    normal_lines_counter += 1
                if re.search(r"[а-яА-Яa-zA-Z0-9–-]$", line):
                    abrupt_lines_counter += 1
            line = f.readline()
    if normal_lines_counter > abrupt_lines_counter:
        result = 'normal'
    if normal_lines_counter < abrupt_lines_counter:
        result = 'abrupter'
    return result


def check_n_fix_newlines_pattern(texts_dir):
    # vars
    text_file_paths: list = []
    # create result filepath
    result_directory_name: str = "preprocessed_files"
    result_path: str = os.path.join(texts_dir, result_directory_name)
    try:
        os.makedirs(result_path, exist_ok=True)
        logger.info(f"Directory <{result_directory_name}> created successfully")
    except OSError as error:
        logger.error(f"Directory <{result_directory_name}> can not be created:\n{error}")
    # walk through the file tree
    for root, directories, files in os.walk(texts_dir):
        for filename in files:
            filepath: str = os.path.join(root, filename)
            text_file_paths.append(filepath)
    # loop through text files paths
    counter = 1
    for txt_file in text_file_paths:
        result_file_name: str = f"{str(counter)}.txt"
        result_file_path: str = os.path.join(result_path, result_file_name)
        tmp_str: list[str] = []
        dialogue_flag: bool = False
        # # check file code page encoding
        # detector = UniversalDetector()
        # with open(txt_file, 'rb') as tf:
        #     for line in tf:
        #         detector.feed(line)
        #         if detector.done:
        #             break
        #     detector.close()
        #     encoding_str = detector.result['encoding']
        #     tf.close()
        with open(result_file_path, 'w', encoding='utf-8') as text:
            with open(txt_file, 'r', encoding='utf-8') as f:  # utf-8 or encoding_str
                pattern: str = check_newlines_pattern(txt_file)
                if pattern == 'normal':
                    for line in f:
                        text.write(line + "\n\n")
                elif pattern == 'abrupter':
                    line = f.readline()
                    while line:
                        if re.match(r"^\s*[-—]\s*[А-ЯA-Z0-9]", line):
                            dialogue_flag = True
                            line.strip()
                            line = re.sub(r"\n", " ", line)
                            tmp_str.append(line)
                        elif re.match(r"^\s*-\s*-\s*[А-ЯA-Z0-9]", line):
                            dialogue_flag = True
                            line.strip()
                            line = re.sub(r"\n", " ", line)
                            tmp_str.append(line)
                        else:
                            if dialogue_flag:
                                line.strip()
                                line = re.sub(r"\n", " ", line)
                                if re.search(r"[.!?]\s*$", line):
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
                else:
                    for line in f:
                        text.write(line + "\n\n")
        counter += 1
