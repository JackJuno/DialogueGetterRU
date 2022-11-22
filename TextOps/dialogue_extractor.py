import os
import re


def clear_dialogue_replica(raw_replica: str) -> str:
    refined_replica = ''
    hyphen = re.compile(r"\s*-\s*")
    dash = re.compile(r"\s*—\s*")
    last_punctuation_marks = re.compile(r"[!?.,;]$")
    end_author_speech = re.compile(r"[.,]$")
    end_of_sentence = re.compile(r"[!?.]$")
    end_coma = re.compile(r"[,;]$")
    # check for hyphen used
    if re.match(r"[\s]*(-)[\s]*[А-Я]", raw_replica):
        tmp_replica = re.sub(r"\s+", " ", raw_replica)
        tmp_instring_position = []
        for m in hyphen.finditer(tmp_replica):
            tmp_instring_position.append(m.start())
        lenth = len(tmp_instring_position)
        # case 1: -Здравствуйте! Я ваш сосед!
        if lenth == 1:
            refined_replica = tmp_replica
        # case 2: -Ай! - и бегом в сторону.
        if lenth == 2:
            tmp_text = tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]
            if last_punctuation_marks.search(tmp_text):
                # clean last char
                if end_coma.search(tmp_text):
                    sub_text = end_coma.sub(r".", tmp_text)
                    refined_replica = sub_text
            else:
                refined_replica = tmp_replica[tmp_instring_position[0]:]
        # case 3: -А что я могу сделать? - сказала она. - Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        if lenth == 3:
            tmp_s = ''
            tmp_a = ''
            tmp_f = ''
            tmp_s_prt = ''
            tmp_a_prt = ''
            s_found = False
            a_found = False
            f_found = False
            for n in range(lenth):
                if n == 0:
                    # check start repl
                    if last_punctuation_marks.search(tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]):
                        tmp_s = tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]
                        s_found = True
                    else:
                        tmp_s_prt = tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]
                if n == 1:
                    # check author repl
                    if s_found and end_author_speech.search(
                            tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]):
                        tmp_a = tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]
                        a_found = True
                    if s_found and not end_author_speech.search(tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]):
                        tmp_a_prt = tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]
                    # check if start repl done
                    if not s_found and last_punctuation_marks.search(
                            tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]):
                        tmp_s = tmp_s_prt + tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]
                        s_found = True
                    if not s_found and not last_punctuation_marks.search(
                            tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]):
                        tmp_s_prt = tmp_s_prt + tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]
                if n == 2:
                    # check finish repl
                    if s_found and a_found:
                        tmp_f = tmp_replica[tmp_instring_position[2]:]
                        f_found = True
                    # check author repl
                    if s_found and not a_found:
                        if tmp_a_prt:
                            tmp_a = tmp_a_prt + tmp_replica[tmp_instring_position[2]:]
                            a_found = True
                    # check start repl
                    if not s_found and not a_found:
                        if tmp_s_prt:
                            tmp_s = tmp_s_prt + tmp_replica[tmp_instring_position[2]:]
                            s_found = True
                        else:
                            tmp_s = tmp_replica[tmp_instring_position[0]:]
                            s_found = True

            if s_found and a_found and f_found:
                # clean refined replica: change coma for dot beetween s & f
                dirty_s = tmp_s
                if end_coma.search(dirty_s):
                    if re.search("^\s*-\s*[А-Я]", tmp_f):
                        sub_text = end_coma.sub(r".", dirty_s)
                        tmp_s = sub_text
                    if re.search("^\s*-\s*[а-я]", tmp_f):
                        sub_text = end_coma.sub(r",", dirty_s)
                        tmp_s = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search("^\s*-\s*[а-я]", tmp_f):
                        tmp_list = []
                        sub_str = re.sub(r"\s*-\s*", " ", tmp_f)
                        first_word, rest = sub_str.split(maxsplit=1)
                        fw = first_word.title()
                        tmp_list.append(fw)
                        tmp_list.append(rest)
                        tmp_f = " ".join(tmp_list)
                refined_replica = tmp_s + " " + re.sub(r"\s*-\s*", "", tmp_f)  # refined_replica = tmp_s + re.sub(r"\s*-\s*", " ", tmp_replica[tmp_instring_position[2]:])
            else:
                refined_replica = tmp_s

            # create dataset for ML: author speech
        #             print(s_found, '\n')
        #             print(tmp_s, '\n')
        #             print(a_found, '\n')
        #             print(tmp_a, '\n')
        #             print(f_found, '\n')
        #             print(tmp_f, '\n')




        # continue



        # case 4:-Ай-ай-ай! - и бегом в сторону.
        if lenth > 3:
            tmp_repl = ''
            tmp_text_start_repl = ''
            tmp_text_author_repl = ''
            tmp_text_last_repl = ''
            punct_count = 0
            position_one = 0
            position_two = 0
            for n in range(lenth):
                if n < lenth - 1:
                    tmp_text_current_part = tmp_replica[tmp_instring_position[n]:tmp_instring_position[n + 1]]
                    if last_punctuation_marks.search(tmp_text_current_part):
                        if punct_count == 1:
                            tmp_repl = tmp_repl + tmp_text_current_part
                            tmp_text_author_repl = tmp_repl
                            position_two = tmp_instring_position[n + 1]
                            tmp_repl = ''
                            punct_count += 1
                        if punct_count == 0:
                            tmp_repl = tmp_repl + tmp_text_current_part
                            tmp_text_start_repl = tmp_repl
                            position_one = tmp_instring_position[n + 1]
                            tmp_repl = ''
                            punct_count += 1
                    else:
                        tmp_repl = tmp_repl + tmp_text_current_part
            if position_one > 0:
                if position_two == 0:
                    tmp_text_last_repl = tmp_replica[position_one:]
                if position_two > 0:
                    tmp_text_last_repl = tmp_replica[position_two:]
            if last_punctuation_marks.search(tmp_text_start_repl) and last_punctuation_marks.search(tmp_text_author_repl):
                refined_replica = tmp_text_start_repl + re.sub(r"\s*-\s*", " ", tmp_text_last_repl[0:])
            else:
                if not tmp_text_author_repl:
                    refined_replica = tmp_text_start_repl

    # check for dash used
    if re.match(r"[\s]*(—)[\s]*[А-Я]", raw_replica):
        tmp_replica = re.sub(r"\s+", " ", raw_replica)
        tmp_instring_position = []
        for m in dash.finditer(tmp_replica):
            tmp_instring_position.append(m.start())
        lenth = len(tmp_instring_position)
        # case 1: —Что же ты, голубушка, делаешь?
        if lenth == 1:
            refined_replica = tmp_replica
        # case 2: —Ай-ай-ай! — и бегом в сторону.
        if lenth == 2:
            tmp_text = tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]
            if last_punctuation_marks.search(tmp_text):
                refined_replica = tmp_text
            else:
                refined_replica = tmp_replica[tmp_instring_position[0]:]
        # case 3: — А что я могу сделать? — сказала она. — Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        if lenth == 3:
            tmp_text_start_repl = tmp_replica[tmp_instring_position[0]:tmp_instring_position[1]]
            tmp_text_author_repl = tmp_replica[tmp_instring_position[1]:tmp_instring_position[2]]
            tmp_text_last_repl = tmp_replica[tmp_instring_position[2]:]
            if last_punctuation_marks.search(tmp_text_start_repl) and last_punctuation_marks.search(tmp_text_author_repl):
                refined_replica = tmp_text_start_repl + re.sub(r"\s*—\s*", " ", tmp_text_last_repl[0:])
       # case 4:-Ай-ай-ай! - и бегом в сторону.
        if lenth > 3:
            tmp_repl = ''
            tmp_text_start_repl = ''
            tmp_text_author_repl = ''
            tmp_text_last_repl = ''
            punct_count = 0
            position_one = 0
            position_two = 0
            for n in range(lenth):
                if n < lenth - 1:
                    tmp_text_current_part = tmp_replica[tmp_instring_position[n]:tmp_instring_position[n + 1]]
                    if last_punctuation_marks.search(tmp_text_current_part):
                        if punct_count == 1:
                            tmp_repl = tmp_repl + tmp_text_current_part
                            tmp_text_author_repl = tmp_repl
                            position_two = int(tmp_instring_position[n + 1])
                            tmp_repl = ''
                            punct_count += 1
                        if punct_count == 0:
                            tmp_repl = tmp_repl + tmp_text_current_part
                            tmp_text_start_repl = tmp_repl
                            position_one = int(tmp_instring_position[n + 1])
                            tmp_repl = ''
                            punct_count += 1
                    else:
                        tmp_repl = tmp_repl + tmp_text_current_part
            if position_one > 0:
                if position_two == 0:
                    tmp_text_last_repl = tmp_replica[position_one:]
                if position_two > 0:
                    tmp_text_last_repl = tmp_replica[position_two:]
            if last_punctuation_marks.search(tmp_text_start_repl) and last_punctuation_marks.search(tmp_text_author_repl):
                refined_replica = tmp_text_start_repl + re.sub(r"\s*-\s*", " ", tmp_text_last_repl[0:])
            else:
                if not tmp_text_author_repl:
                    refined_replica = tmp_text_start_repl

    return refined_replica


def check_for_embeded_replicas(raw_line: str) -> list:
    result = []
    return result


# extract & save dialogues
def extract_n_save_replicas(src_path, dataset_path):
    source_files_paths = []
    dialogue_list: list = []
    # open dir with preprocessed file
    subdir_one = "automatically_created_copies_of_utf_encoded_files"
    subdir_two = "preprocessed_files"
    source_path_dir_tmp = os.path.join(src_path, subdir_one)
    source_path_dir = os.path.join(source_path_dir_tmp, subdir_two)
    for root, directories, files in os.walk(source_path_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            source_files_paths.append(filepath)
    counter = 1
    for path in source_files_paths:
        dataset_file_name = f"dataset_{str(counter)}.txt"
        dataset_file_path = os.path.join(dataset_path, dataset_file_name)
        with open(dataset_file_path, 'w', encoding='utf-8') as storage:
            with open(path, 'r', encoding='utf-8') as text:
                for line in text:
                    # find replica
                    if line == r"\n\n":
                        continue
                    elif line == r"\n":
                        continue
                    elif line == r"\r":
                        continue
                    elif re.match(r"^(\s*)(-|—)(\s*)[А-Я]", line):
                        # a possible dialogue line has been found
                        # check for embeded replicas
                        embedded_replicas = check_for_embeded_replicas(line)
                        if embedded_replicas:
                            # write them down to tmp dialogue_list
                            for item in embedded_replicas:
                                # clear dialogue replica
                                replica = clear_dialogue_replica(item)
                                # write down replica to tmp dialogue_list
                                dialogue_list.append(replica)
                        else:
                            # clear dialogue replica
                            replica = clear_dialogue_replica(line)
                            # write down replica to tmp dialogue_list
                            dialogue_list.append(replica)
                    elif re.match(r"^(\s*)[А-Я]", line):
                        if len(dialogue_list) >= 2:
                            # write down dialogue list to file line, line, \n
                            for n in range(len(dialogue_list)):
                                if n < len(dialogue_list) - 1:
                                    storage.write(dialogue_list[n] + '\n')
                                    storage.write(dialogue_list[n + 1] + '\n')
                                    storage.write('\n')
                            dialogue_list = []
                        if len(dialogue_list) == 1:
                            dialogue_list = []
        counter+=1

# extract_n_save_replicas('/home/zonengeistbot/Documents/test_1', '/home/zonengeistbot/Documents/dtset_test')