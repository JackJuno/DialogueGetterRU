import os
import re


def last_replica_simple(rpl, re_obj):
    hyphen = ' - '
    dash = ' — '
    result: bool = True
    re_obj_position: list = []
    s_fnd = False
    a_fnd = False
    if re.match(r"^\s*[-—]\s*", rpl):
        for i in re_obj.finditer(rpl):
            re_obj_position.append(i.start())
        length = len(re_obj_position)
        if length == 1:
            return result
        else:
            for x in range(length):
                if x == 0:
                    current_line_zero: str = rpl[re_obj_position[0]:re_obj_position[1]]
                    # search for dir spch with grammatically right punctuation mark
                    if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$", current_line_zero):
                        s_fnd = True
                    # search for dir spch with grammatically wrong punctuation mark
                    elif re.search(r"\s*\.\s*$", current_line_zero):
                        s_fnd = True
                elif x == length - 1:
                    if s_fnd:
                        a_fnd = True
                else:
                    # var for current part of replica
                    current_line_x = rpl[re_obj_position[x]:re_obj_position[x + 1]]
                    if s_fnd and a_fnd:
                        break
                    elif s_fnd:
                        # search for author replica with dot in the middle
                        if re.search(r"\w\s*\.\s*\w", current_line_x):
                            if re.search(r"[.!?:]$", current_line_x):
                                a_fnd = True
                        else:
                            # search for normal author replica end
                            if re.search(r"[.,]$", current_line_x):
                                a_fnd = True
                    else:
                        # search for dir spch with grammatically right punctuation mark
                        if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$", current_line_x):
                            s_fnd = True
                        # search for dir spch with grammatically wrong punctuation mark
                        elif re.search(r"\s*\.\s*$", current_line_x):
                            s_fnd = True
    else:
        if re_obj.search(hyphen):
            new_rpl_h: str = hyphen + rpl
            for i in re_obj.finditer(new_rpl_h):
                re_obj_position.append(i.start())
            length = len(re_obj_position)
            if length == 1:
                return result
            else:
                for x in range(length):
                    if x == 0:
                        current_line_zero: str = new_rpl_h[re_obj_position[0]:re_obj_position[1]]
                        # search for dir spch with grammatically right punctuation mark
                        if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$",
                                     current_line_zero):
                            s_fnd = True
                        # search for dir spch with grammatically wrong punctuation mark
                        elif re.search(r"\s*\.\s*$", current_line_zero):
                            s_fnd = True
                    elif x == length - 1:
                        if s_fnd:
                            a_fnd = True
                    else:
                        # var for current part of replica
                        current_line_x = new_rpl_h[re_obj_position[x]:re_obj_position[x + 1]]
                        if s_fnd and a_fnd:
                            break
                        elif s_fnd:
                            # search for author replica with dot in the middle
                            if re.search(r"\w\s*\.\s*\w", current_line_x):
                                if re.search(r"[.!?:]$", current_line_x):
                                    a_fnd = True
                            else:
                                # search for normal author replica end
                                if re.search(r"[.,]$", current_line_x):
                                    a_fnd = True
                        else:
                            # search for dir spch with grammatically right punctuation mark
                            if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$",
                                         current_line_x):
                                s_fnd = True
                            # search for dir spch with grammatically wrong punctuation mark
                            elif re.search(r"\s*\.\s*$", current_line_x):
                                s_fnd = True
        if re_obj.search(dash):
            new_rpl_d: str = dash + rpl
            for i in re_obj.finditer(new_rpl_d):
                re_obj_position.append(i.start())
            length = len(re_obj_position)
            if length == 1:
                return result
            else:
                for x in range(length):
                    if x == 0:
                        current_line_zero: str = new_rpl_d[re_obj_position[0]:re_obj_position[1]]
                        # search for dir spch with grammatically right punctuation mark
                        if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$",
                                     current_line_zero):
                            s_fnd = True
                        # search for dir spch with grammatically wrong punctuation mark
                        elif re.search(r"\s*\.\s*$", current_line_zero):
                            s_fnd = True
                    elif x == length - 1:
                        if s_fnd:
                            a_fnd = True
                    else:
                        # var for current part of replica
                        current_line_x = new_rpl_d[re_obj_position[x]:re_obj_position[x + 1]]
                        if s_fnd and a_fnd:
                            break
                        elif s_fnd:
                            # search for author replica with dot in the middle
                            if re.search(r"\w\s*\.\s*\w", current_line_x):
                                if re.search(r"[.!?:]$", current_line_x):
                                    a_fnd = True
                            else:
                                # search for normal author replica end
                                if re.search(r"[.,]$", current_line_x):
                                    a_fnd = True
                        else:
                            # search for dir spch with grammatically right punctuation mark
                            if re.search(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$",
                                         current_line_x):
                                s_fnd = True
                            # search for dir spch with grammatically wrong punctuation mark
                            elif re.search(r"\s*\.\s*$", current_line_x):
                                s_fnd = True
    if s_fnd and a_fnd:
        result = False
    return result


def check_for_five_more_spaces(sentence: str) -> str:
    possible_replica = re.compile(r"[ ]{5,}[-—]\s*[А-ЯA-Z0-9]")
    five_more_spaces = re.compile(r"[ ]{5,}")
    if possible_replica.search(sentence):
        list_of_parts = sentence.split("     ")
        sentence = "\n".join(list_of_parts)
        # sentence = five_more_spaces.sub(r"\n", sentence)
    return sentence


def process_fin_replica_subreplicas(text_in: str) -> str:
    result_str: str = ""
    hyphen = re.compile(r"\s*-\s*")
    dash = re.compile(r"\s*—\s*")
    dot_in_the_middle = re.compile(r"\w\s*\.\s*\w")
    dot_in_the_end = re.compile(r"\s*\.\s*$")
    last_punctuation_mark = re.compile(r"[!?.,]$")
    end_of_start_replica = re.compile(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$")
    end_of_author_speech = re.compile(r"[.,]$")
    end_of_author_speech_long = re.compile(r"[.!?:]$")
    end_of_sentence = re.compile(r"[!?.]$")
    end_coma = re.compile(r"[,;]$")
    tmp_text_case_two: str = ""
    replica_subreplicas_list = []
    # check for hyphen used as a start of dialogue mark: separate processing of hyphen and dash substantiated by practice
    if re.match(r"^\s*-\s*[А-ЯA-Z0-9]", text_in):
        # put a replica to tmp var for further processing
        tmp_replica: str = re.sub(r"\s+", " ", text_in)
        # prepare a list with hyphen positions <int> in the replica
        instring_position = []
        # populate the list with ints of start positions of hyphens met
        for m in hyphen.finditer(tmp_replica):
            instring_position.append(m.start())
        # length is a number of huphens found
        length = len(instring_position)
        # Case 1: -Здравствуйте! Я ваш сосед! / "-D.", "-D..." "-D!", "-D?"
        if length == 1:
            result_str = tmp_replica
            # refined replica returns: "-D"
        # Case 2: -Ай! - и бегом в сторону. / "-D,-a.", "-D?-a.", "-D!-a.", "-D...-a." or "-D-d."
        if length == 2:
            # tmp text is a part from first to start of second hyphen
            tmp_text_case_two: str = tmp_replica[instring_position[0]:instring_position[1]]
            # firstly process cases with Direct & Author speeches: grammatically right
            if end_of_start_replica.search(tmp_text_case_two):
                result_str = tmp_text_case_two
                # result_str returns: "-D,", "-D?", "-D!", "-D..."
            # process cases with Direct & Author speeches: grammatically wrong
            elif dot_in_the_end.search(tmp_text_case_two):
                result_str = tmp_text_case_two
                # result_str returns: "-D."
            else:
                # process cases with Direct speeches with hyphen in the middle
                if end_of_sentence.search(tmp_replica[instring_position[1]:]):
                    result_str = tmp_replica[instring_position[0]:]
                else:
                    result_str = tmp_replica[instring_position[0]:]
                    # result_str returns: "-D-d.!?"
        # Case 3: -А что я могу сделать? - сказала она. - Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        # "-D[,!?...][.]-a[.,]- D/d[.!?]", "—D[,!?...][.]—а.А[:.!?]—D." or "-D-d[,!?...][.]-a." or "-D[,!?...][.]-a-a." or "-D-d-d[.!?...]"
        if length == 3:
            # prepare vars for patterns search
            tmp_s_case_three: str = ''
            tmp_a_case_three: str = ''
            tmp_f_case_three: str = ''
            tmp_s_prt_case_three: str = ''
            tmp_a_prt_case_three: str = ''
            s_found_case_three: bool = False
            a_found_case_three: bool = False
            f_found_case_three: bool = False
            # loop trough hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                if n == 0:
                    # apparently the replica starts with direct speech: check for its boundaries
                    # check if start part coincide with first part of direct speech: grammatically right
                    if end_of_start_replica.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D[,!?...]"
                    # check if start part coincide with first part of direct speech: grammatically wrong
                    elif dot_in_the_end.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D."
                    # if not, then possible pattern is "-D-d[,!?...]-a."
                    else:
                        # put the first part in tmp var for use in the next step
                        tmp_s_prt_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                if n == 1:
                    # on the second step firstly check the "start repl found" case
                    if s_found_case_three:
                        # check if current part is an author repl. Possible patterns: —а.А[:.!?] & -a[.,]
                        if dot_in_the_middle.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then possible patterns: —а.А[:.!?]
                            if end_of_author_speech_long.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: —а.А[:.!?]
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                        # if no dot in the middle, then check for normal author speech pattern
                        else:
                            if end_of_author_speech.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: "-a[.,]"
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                    # now check the "start repl not found" case
                    if s_found_case_three == False:
                        # check if current part is an end of grammatically right start repl
                        if end_of_start_replica.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then start repl found
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d[,!?...]"
                        # check if current part is an end of grammatically wrong start repl
                        elif dot_in_the_end.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes than we found start part
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d."
                        # if not, then possible pattern is "-D-d-d[.!?...]"
                        else:
                            # put the first two parts in tmp var for use in the next step
                            tmp_s_prt_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                          instring_position[1]:instring_position[2]]
                if n == 2:
                    # in the last step firstly check the "start repl found" & "author repl found" case
                    if s_found_case_three and a_found_case_three:
                        # apparently current part is a finish part
                        f_found_case_three = True
                        tmp_f_case_three = tmp_replica[instring_position[2]:]
                        # tmp_f_case_three returns: "- D/d[.!?]" or "-D."
                    # check the "start repl found" & "author repl not found" case
                    elif s_found_case_three:
                        # check for possible pattern "-D[,!?...]-a-a." or "-D-d[,!?...][.]-a."
                        if dot_in_the_end.search(tmp_replica[instring_position[2]:]):
                            # if yes we found author speech. Possible patterns: "-a-a."  or "-a."
                            if tmp_a_prt_case_three:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_a_prt_case_three + tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a-a."
                            else:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a."
                    # check the "start repl not found" case
                    elif s_found_case_three == False:
                        # check for possible pattern "-D-d-d[.!?...]"
                        if end_of_sentence.search(tmp_replica[instring_position[2]:]):
                            # if yes than we found full start repl
                            s_found_case_three = True
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[instring_position[2]:]
                            # tmp_s_case_three returns: "-D-d-d[.!?...]"
            # now let`s construct refined replica to return
            if s_found_case_three and a_found_case_three and f_found_case_three:
                # clean parts of replica: change coma for dot beetween s & f
                dirty_s = tmp_s_case_three
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*-\s*[А-Я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r".", dirty_s)
                        tmp_s_case_three = sub_text
                    elif re.search(r"^\s*-\s*[а-я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r",", dirty_s)
                        tmp_s_case_three = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*-\s*[а-я]", tmp_f_case_three):
                        tmp_list = []
                        sub_str = re.sub(r"\s*-\s*", " ", tmp_f_case_three)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        tmp_f_case_three = " ".join(tmp_list)
                result_str = tmp_s_case_three + " " + re.sub(r"\s*-\s*", " ", tmp_f_case_three)
            else:
                result_str = tmp_s_case_three
        # case 4:-Ай-ай-ай! - и бегом в сторону.
        # unpredictable number of hyphens in a replica "-D-d-d, -a-a. -D-d-d-d. -a. -D. -A."
        if length > 3:
            # initiate vars
            s_case_four: str = ''
            a_case_four: str = ''
            f_case_four: str = ''
            s_prt_case_four: str = ''
            a_prt_case_four: str = ''
            f_prt_case_four: str = ''
            current_prt_case_four: str = ''
            # candidate_s_prt_case_four: str = ''
            candidate_finish_prt_case_four: str = ''
            replica_candidate_patterns: list = []
            s_found_case_four: bool = False
            a_found_case_four: bool = False
            f_found_case_four: bool = False
            # iterate through hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                # check the first occurance
                if n == 0:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[0]:instring_position[1]]
                    # check if the first part is a start repl: grammatically right
                    if end_of_start_replica.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # D, d - direct speech, A,a - author speech
                        # replica_candidate_patterns = ["-D,-a.", "-D?-a.", "-D!-a.", "-D...-a."]
                    # grammatically wrong but used by some authors pattern
                    elif dot_in_the_end.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # replica_candidate_patterns = ["-D.-a."]
                    else:
                        s_prt_case_four = current_prt_case_four
                # check last occurence
                elif n == length - 1:
                    current_prt_case_four = tmp_replica[instring_position[n]:]
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        break
                    elif s_found_case_four and a_found_case_four:
                        f_found_case_four = True
                        f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        if a_prt_case_four:
                            a_found_case_four = True
                            a_case_four = a_prt_case_four + current_prt_case_four
                        else:
                            a_found_case_four = True
                            a_case_four = current_prt_case_four
                    else:
                        # end of replica start part still not found
                        if s_prt_case_four:
                            s_found_case_four = True
                            s_case_four = s_prt_case_four + current_prt_case_four
                        else:
                            s_found_case_four = True
                            s_case_four = current_prt_case_four
                else:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[n]:instring_position[n + 1]]
                    # define current position in the vertual flow
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        continue
                    elif s_found_case_four and a_found_case_four:
                        # check if final part by chance enriched with dir spch & auth spch or not
                        candidate_finish_prt_case_four = tmp_replica[instring_position[n]:]
                        if last_replica_simple(candidate_finish_prt_case_four, hyphen):
                            # rpl is simple: just add
                            f_found_case_four = True
                            f_case_four = candidate_finish_prt_case_four
                        else:
                            # there are more dialogues in rpl: needs process
                            replica_deconstruction_result = process_fin_replica_subreplicas(candidate_finish_prt_case_four)
                            if replica_deconstruction_result:
                                f_found_case_four = True
                                f_case_four = replica_deconstruction_result
                            # Just in case
                            else:
                                f_found_case_four = True
                                f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        # divide fist time cases and multiply cases
                        if a_prt_case_four:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a,-d."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                        # the first time check
                        else:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a,-d."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                    else:
                        # start part still not found
                        if s_prt_case_four:
                            # check if the cerrent prt is an end of start part
                            if end_of_start_replica.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # D, d - direct speech, A,a - author speech
                                # replica_candidate_patterns = ["-D-d,-a.", "-D-d?-a.", "-D-d!-a.", "-D-d...-a."]
                            # check grammatically wrong but used by some authors puttern
                            elif dot_in_the_end.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d.-a."]
                            # If end of start replica still not found, then put current repl to s_prt_case_four
                            else:
                                s_prt_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d-d."]
            if s_found_case_four and a_found_case_four and f_found_case_four:
                # clean refined replica: change coma for dot between s & f parts
                dirty_s = s_case_four
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*-\s*[А-Я]", f_case_four):
                        sub_text = end_coma.sub(r".", dirty_s)
                        s_case_four = sub_text
                    if re.search(r"^\s*-\s*[а-я]", f_case_four):
                        sub_text = end_coma.sub(r",", dirty_s)
                        s_case_four = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*-\s*[а-я]", f_case_four):
                        tmp_list = []
                        sub_str = re.sub(r"\s*-\s*", " ", f_case_four)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        f_case_four = " ".join(tmp_list)
                result_str = s_case_four + " " + re.sub(r"\s*-\s*", " ", f_case_four)
            else:
                result_str = s_case_four
    # check for dash
    if re.match(r"^\s*—\s*[А-ЯA-Z0-9]", text_in):
        # put a replica to tmp var for further processing
        tmp_replica: str = re.sub(r"\s+", " ", text_in)
        # prepare a list with hyphen positions <int> in the replica
        instring_position = []
        # populate the list with ints of start positions of hyphens met
        for m in dash.finditer(tmp_replica):
            instring_position.append(m.start())
        # length is a number of huphens found
        length = len(instring_position)
        # Case 1: -Здравствуйте! Я ваш сосед! / "-D.", "-D..." "-D!", "-D?"
        if length == 1:
            result_str = tmp_replica
            # refined replica returns: "-D"
        # Case 2: -Ай! - и бегом в сторону. / "-D,-a.", "-D?-a.", "-D!-a.", "-D...-a." or "-D-d."
        if length == 2:
            # tmp text is a part from first to start of second hyphen
            tmp_text_case_two: str = tmp_replica[instring_position[0]:instring_position[1]]
            # firstly process cases with Direct & Author speeches: grammatically right
            if end_of_start_replica.search(tmp_text_case_two):
                result_str = tmp_text_case_two
                # result_str returns: "-D,", "-D?", "-D!", "-D..."
            # process cases with Direct & Author speeches: grammatically wrong
            elif dot_in_the_end.search(tmp_text_case_two):
                result_str = tmp_text_case_two
                # result_str returns: "-D."
            else:
                # process cases with Direct speeches with hyphen in the middle
                if end_of_sentence.search(tmp_replica[instring_position[1]:]):
                    result_str = tmp_replica[instring_position[0]:]
                else:
                    result_str = tmp_replica[instring_position[0]:]
                    # result_str returns: "-D-d.!?"
        # Case 3: -А что я могу сделать? - сказала она. - Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        # "-D[,!?...][.]-a[.,]- D/d[.!?]", "—D[,!?...][.]—а.А[:.!?]—D." or "-D-d[,!?...][.]-a." or "-D[,!?...][.]-a-a." or "-D-d-d[.!?...]"
        if length == 3:
            # prepare vars for patterns search
            tmp_s_case_three: str = ''
            tmp_a_case_three: str = ''
            tmp_f_case_three: str = ''
            tmp_s_prt_case_three: str = ''
            tmp_a_prt_case_three: str = ''
            s_found_case_three: bool = False
            a_found_case_three: bool = False
            f_found_case_three: bool = False
            # loop trough hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                if n == 0:
                    # apparently the replica starts with direct speech: check for its boundaries
                    # check if start part coincide with first part of direct speech: grammatically right
                    if end_of_start_replica.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D[,!?...]"
                    # check if start part coincide with first part of direct speech: grammatically wrong
                    elif dot_in_the_end.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D."
                    # if not, then possible pattern is "-D-d[,!?...]-a."
                    else:
                        # put the first part in tmp var for use in the next step
                        tmp_s_prt_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                if n == 1:
                    # on the second step firstly check the "start repl found" case
                    if s_found_case_three:
                        # check if current part is an author repl. Possible patterns: —а.А[:.!?] & -a[.,]
                        if dot_in_the_middle.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then possible patterns: —а.А[:.!?]
                            if end_of_author_speech_long.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: —а.А[:.!?]
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                        # if no dot in the middle, then check for normal author speech pattern
                        else:
                            if end_of_author_speech.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: "-a[.,]"
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                    # now check the "start repl not found" case
                    if s_found_case_three == False:
                        # check if current part is an end of grammatically right start repl
                        if end_of_start_replica.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then start repl found
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d[,!?...]"
                        # check if current part is an end of grammatically wrong start repl
                        elif dot_in_the_end.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes than we found start part
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d."
                        # if not, then possible pattern is "-D-d-d[.!?...]"
                        else:
                            # put the first two parts in tmp var for use in the next step
                            tmp_s_prt_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                          instring_position[1]:instring_position[2]]
                if n == 2:
                    # in the last step firstly check the "start repl found" & "author repl found" case
                    if s_found_case_three and a_found_case_three:
                        # apparently current part is a finish part
                        f_found_case_three = True
                        tmp_f_case_three = tmp_replica[instring_position[2]:]
                        # tmp_f_case_three returns: "- D/d[.!?]" or "-D."
                    # check the "start repl found" & "author repl not found" case
                    elif s_found_case_three:
                        # check for possible pattern "-D[,!?...]-a-a." or "-D-d[,!?...][.]-a."
                        if dot_in_the_end.search(tmp_replica[instring_position[2]:]):
                            # if yes we found author speech. Possible patterns: "-a-a."  or "-a."
                            if tmp_a_prt_case_three:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_a_prt_case_three + tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a-a."
                            else:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a."
                    # check the "start repl not found" case
                    elif s_found_case_three == False:
                        # check for possible pattern "-D-d-d[.!?...]"
                        if end_of_sentence.search(tmp_replica[instring_position[2]:]):
                            # if yes than we found full start repl
                            s_found_case_three = True
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[instring_position[2]:]
                            # tmp_s_case_three returns: "-D-d-d[.!?...]"
            # now let`s construct refined replica to return
            if s_found_case_three and a_found_case_three and f_found_case_three:
                # clean parts of replica: change coma for dot beetween s & f
                dirty_s = tmp_s_case_three
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*—\s*[А-Я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r".", dirty_s)
                        tmp_s_case_three = sub_text
                    elif re.search(r"^\s*—\s*[а-я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r",", dirty_s)
                        tmp_s_case_three = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*—\s*[а-я]", tmp_f_case_three):
                        tmp_list = []
                        sub_str = re.sub(r"\s*—\s*", " ", tmp_f_case_three)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        tmp_f_case_three = " ".join(tmp_list)
                result_str = tmp_s_case_three + " " + re.sub(r"\s*—\s*", " ", tmp_f_case_three)
            else:
                result_str = tmp_s_case_three
        # case 4:-Ай-ай-ай! - и бегом в сторону.
        # unpredictable number of hyphens in a replica "-D-d-d, -a-a. -D-d-d-d. -a. -D. -A."
        if length > 3:
            # initiate vars
            s_case_four: str = ''
            a_case_four: str = ''
            f_case_four: str = ''
            s_prt_case_four: str = ''
            a_prt_case_four: str = ''
            f_prt_case_four: str = ''
            current_prt_case_four: str = ''
            # candidate_s_prt_case_four: str = ''
            candidate_finish_prt_case_four: str = ''
            replica_candidate_patterns: list = []
            s_found_case_four: bool = False
            a_found_case_four: bool = False
            f_found_case_four: bool = False
            # iterate through hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                # check the first occurance
                if n == 0:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[0]:instring_position[1]]
                    # check if the first part is a start repl: grammatically right
                    if end_of_start_replica.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # D, d - direct speech, A,a - author speech
                        # replica_candidate_patterns = ["-D,-a.", "-D?-a.", "-D!-a.", "-D...-a."]
                    # grammatically wrong but used by some authors pattern
                    elif dot_in_the_end.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # replica_candidate_patterns = ["-D.-a."]
                    else:
                        s_prt_case_four = current_prt_case_four
                # check last occurence
                elif n == length - 1:
                    current_prt_case_four = tmp_replica[instring_position[n]:]
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        break
                    elif s_found_case_four and a_found_case_four:
                        f_found_case_four = True
                        f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        if a_prt_case_four:
                            a_found_case_four = True
                            a_case_four = a_prt_case_four + current_prt_case_four
                        else:
                            a_found_case_four = True
                            a_case_four = current_prt_case_four
                    else:
                        # end of replica start part still not found
                        if s_prt_case_four:
                            s_found_case_four = True
                            s_case_four = s_prt_case_four + current_prt_case_four
                        else:
                            s_found_case_four = True
                            s_case_four = current_prt_case_four
                else:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[n]:instring_position[n + 1]]
                    # define current position in the vertual flow
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        continue
                    elif s_found_case_four and a_found_case_four:
                        # check if final part by chance enriched with dir spch & auth spch or not
                        candidate_finish_prt_case_four = tmp_replica[instring_position[n]:]
                        if last_replica_simple(candidate_finish_prt_case_four, dash):
                            # rpl is simple: just add
                            f_found_case_four = True
                            f_case_four = candidate_finish_prt_case_four
                        else:
                            # there are more dialogues in rpl: needs process
                            replica_deconstruction_result = process_fin_replica_subreplicas(
                                candidate_finish_prt_case_four)
                            if replica_deconstruction_result:
                                f_found_case_four = True
                                f_case_four = replica_deconstruction_result
                            # Just in case
                            else:
                                f_found_case_four = True
                                f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        # divide fist time cases and multiply cases
                        if a_prt_case_four:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a,-d."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                        # the first time check
                        else:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a,-d."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                    else:
                        # start part still not found
                        if s_prt_case_four:
                            # check if the cerrent prt is an end of start part
                            if end_of_start_replica.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # D, d - direct speech, A,a - author speech
                                # replica_candidate_patterns = ["-D-d,-a.", "-D-d?-a.", "-D-d!-a.", "-D-d...-a."]
                            # check grammatically wrong but used by some authors puttern
                            elif dot_in_the_end.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d.-a."]
                            # If end of start replica still not found, then put current repl to s_prt_case_four
                            else:
                                s_prt_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d-d."]
            if s_found_case_four and a_found_case_four and f_found_case_four:
                # clean refined replica: change coma for dot between s & f parts
                dirty_s = s_case_four
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*—\s*[А-Я]", f_case_four):
                        sub_text = end_coma.sub(r".", dirty_s)
                        s_case_four = sub_text
                    if re.search(r"^\s*—\s*[а-я]", f_case_four):
                        sub_text = end_coma.sub(r",", dirty_s)
                        s_case_four = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*—\s*[а-я]", f_case_four):
                        tmp_list = []
                        sub_str = re.sub(r"\s*—\s*", " ", f_case_four)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        f_case_four = " ".join(tmp_list)
                result_str = s_case_four + " " + re.sub(r"\s*—\s*", " ", f_case_four)
            else:
                result_str = s_case_four
    return result_str


# create dataset for ML: author speech
#             print(s_found, '\n')
#             print(tmp_s, '\n')
#             print(a_found, '\n')
#             print(tmp_a, '\n')
#             print(f_found, '\n')
#             print(tmp_f, '\n')

def clear_dialogue_replica(raw_replica: str) -> str:
    refined_replica: str = ""
    hyphen_o_dash = (r"\s*[-—]\s*")
    hyphen = re.compile(r"\s*-\s*")
    dash = re.compile(r"\s*—\s*")
    dot_in_the_middle = re.compile(r"\w\s*\.\s*\w")
    dot_in_the_end = re.compile(r"\s*\.\s*$")
    last_punctuation_mark = re.compile(r"[!?.,]$")
    end_of_start_replica = re.compile(r"\s*[!?,]\s*$|\s*\.{3}\s*$|\s*…\s*$|\s*!\.\.\s*$|\s*\?\.\.\s*$")
    end_of_author_speech = re.compile(r"[.,]$")
    end_of_author_speech_long = re.compile(r"[.!?:]$")
    end_of_sentence = re.compile(r"[!?.]$")
    end_coma = re.compile(r"[,;]$")
    tmp_text_case_two: str = ""
    replica_subreplicas_list = []
    # check for hyphen used as a start of dialogue mark: separate processing of hyphen and dash substantiated by practice
    if re.match(r"^\s*-\s*[А-ЯA-Z0-9]", raw_replica):
        # put a replica to tmp var for further processing
        tmp_replica: str = re.sub(r"\s+", " ", raw_replica)
        # prepare a list with hyphen positions <int> in the replica
        instring_position = []
        # populate the list with ints of start positions of hyphens met
        for m in hyphen.finditer(tmp_replica):
            instring_position.append(m.start())
        # length is a number of huphens found
        length = len(instring_position)
        # Case 1: -Здравствуйте! Я ваш сосед! / "-D.", "-D..." "-D!", "-D?"
        if length == 1:
            refined_replica = tmp_replica
            # refined replica returns: "-D"
        # Case 2: -Ай! - и бегом в сторону. / "-D,-a.", "-D?-a.", "-D!-a.", "-D...-a." or "-D-d."
        if length == 2:
            # tmp text is a part from first to start of second hyphen
            tmp_text_case_two: str = tmp_replica[instring_position[0]:instring_position[1]]
            # firstly process cases with Direct & Author speeches: grammatically right
            if end_of_start_replica.search(tmp_text_case_two):
                refined_replica = tmp_text_case_two
                # refined replica returns: "-D,", "-D?", "-D!", "-D..."
            # process cases with Direct & Author speeches: grammatically wrong
            elif dot_in_the_end.search(tmp_text_case_two):
                refined_replica = tmp_text_case_two
                # refined replica returns: "-D."
            else:
                # process cases with Direct speeches with hyphen in the middle
                if end_of_sentence.search(tmp_replica[instring_position[1]:]):
                    refined_replica = tmp_replica[instring_position[0]:]
                else:
                    refined_replica = tmp_replica[instring_position[0]:]
                    # refined replica returns: "-D-d.!?"
        # Case 3: -А что я могу сделать? - сказала она. - Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        # "-D[,!?...][.]-a[.,]- D/d[.!?]", "—D[,!?...][.]—а.А[:.!?]—D." or "-D-d[,!?...][.]-a." or "-D[,!?...][.]-a-a." or "-D-d-d[.!?...]"
        if length == 3:
            # prepare vars for patterns search
            tmp_s_case_three: str = ''
            tmp_a_case_three: str = ''
            tmp_f_case_three: str = ''
            tmp_s_prt_case_three: str = ''
            tmp_a_prt_case_three: str = ''
            s_found_case_three: bool = False
            a_found_case_three: bool = False
            f_found_case_three: bool = False
            # loop trough hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                if n == 0:
                    # apparently the replica starts with direct speech: check for its boundaries
                    # check if start part coincide with first part of direct speech: grammatically right
                    if end_of_start_replica.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D[,!?...]"
                    # check if start part coincide with first part of direct speech: grammatically wrong
                    elif dot_in_the_end.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D."
                    # if not, then possible pattern is "-D-d[,!?...]-a."
                    else:
                        # put the first part in tmp var for use in the next step
                        tmp_s_prt_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                if n == 1:
                    # on the second step firstly check the "start repl found" case
                    if s_found_case_three:
                        # check if current part is an author repl. Possible patterns: —а.А[:.!?] & -a[.,]
                        if dot_in_the_middle.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then possible patterns: —а.А[:.!?]
                            if end_of_author_speech_long.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: —а.А[:.!?]
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                        # if no dot in the middle, then check for normal author speech pattern
                        else:
                            if end_of_author_speech.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: "-a[.,]"
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                    # now check the "start repl not found" case
                    if s_found_case_three == False:
                        # check if current part is an end of grammatically right start repl
                        if end_of_start_replica.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then start repl found
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d[,!?...]"
                        # check if current part is an end of grammatically wrong start repl
                        elif dot_in_the_end.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes than we found start part
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d."
                        # if not, then possible pattern is "-D-d-d[.!?...]"
                        else:
                            # put the first two parts in tmp var for use in the next step
                            tmp_s_prt_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                          instring_position[1]:instring_position[2]]
                if n == 2:
                    # in the last step firstly check the "start repl found" & "author repl found" case
                    if s_found_case_three and a_found_case_three:
                        # apparently current part is a finish part
                        f_found_case_three = True
                        tmp_f_case_three = tmp_replica[instring_position[2]:]
                        # tmp_f_case_three returns: "- D/d[.!?]" or "-D."
                    # check the "start repl found" & "author repl not found" case
                    elif s_found_case_three:
                        # check for possible pattern "-D[,!?...]-a-a." or "-D-d[,!?...][.]-a."
                        if dot_in_the_end.search(tmp_replica[instring_position[2]:]):
                            # if yes we found author speech. Possible patterns: "-a-a."  or "-a."
                            if tmp_a_prt_case_three:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_a_prt_case_three + tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a-a."
                            else:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a."
                    # check the "start repl not found" case
                    elif s_found_case_three == False:
                        # check for possible pattern "-D-d-d[.!?...]"
                        if end_of_sentence.search(tmp_replica[instring_position[2]:]):
                            # if yes than we found full start repl
                            s_found_case_three = True
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[instring_position[2]:]
                            # tmp_s_case_three returns: "-D-d-d[.!?...]"
            # now let`s construct refined replica to return
            if s_found_case_three and a_found_case_three and f_found_case_three:
                # clean parts of replica: change coma for dot beetween s & f
                dirty_s = tmp_s_case_three
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*-\s*[А-Я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r".", dirty_s)
                        tmp_s_case_three = sub_text
                    elif re.search(r"^\s*-\s*[а-я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r",", dirty_s)
                        tmp_s_case_three = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*-\s*[а-я]", tmp_f_case_three):
                        tmp_list = []
                        sub_str = re.sub(r"\s*-\s*", " ", tmp_f_case_three)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        tmp_f_case_three = " ".join(tmp_list)
                refined_replica = tmp_s_case_three + " " + re.sub(r"\s*-\s*", " ", tmp_f_case_three)
            else:
                refined_replica = tmp_s_case_three
        # case 4:-Ай-ай-ай! - и бегом в сторону.
        # unpredictable number of hyphens in a replica "-D-d-d, -a-a. -D-d-d-d. -a. -D. -A."
        if length > 3:
            # initiate vars
            s_case_four: str = ''
            a_case_four: str = ''
            f_case_four: str = ''
            s_prt_case_four: str = ''
            a_prt_case_four: str = ''
            f_prt_case_four: str = ''
            current_prt_case_four: str = ''
            # candidate_s_prt_case_four: str = ''
            candidate_finish_prt_case_four: str = ''
            replica_candidate_patterns: list = []
            s_found_case_four: bool = False
            a_found_case_four: bool = False
            f_found_case_four: bool = False
            # iterate through hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                # check the first occurance
                if n == 0:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[0]:instring_position[1]]
                    # check if the first part is a start repl: grammatically right
                    if end_of_start_replica.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # D, d - direct speech, A,a - author speech
                        # replica_candidate_patterns = ["-D,-a.", "-D?-a.", "-D!-a.", "-D...-a."]
                    # grammatically wrong but used by some authors pattern
                    elif dot_in_the_end.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # replica_candidate_patterns = ["-D.-a."]
                    else:
                        s_prt_case_four = current_prt_case_four
                # check last occurence
                elif n == length - 1:
                    current_prt_case_four = tmp_replica[instring_position[n]:]
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        break
                    elif s_found_case_four and a_found_case_four:
                        f_found_case_four = True
                        f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        if a_prt_case_four:
                            a_found_case_four = True
                            a_case_four = a_prt_case_four + current_prt_case_four
                        else:
                            a_found_case_four = True
                            a_case_four = current_prt_case_four
                    else:
                        # end of replica start part still not found
                        if s_prt_case_four:
                            s_found_case_four = True
                            s_case_four = s_prt_case_four + current_prt_case_four
                        else:
                            s_found_case_four = True
                            s_case_four = current_prt_case_four
                else:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[n]:instring_position[n + 1]]
                    # define current position in the vertual flow
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        continue
                    elif s_found_case_four and a_found_case_four:
                        # check if final part by chance enriched with dir spch & auth spch or not
                        candidate_finish_prt_case_four = tmp_replica[instring_position[n]:]
                        if last_replica_simple(candidate_finish_prt_case_four, hyphen):
                            # rpl is simple: just add
                            f_found_case_four = True
                            f_case_four = candidate_finish_prt_case_four
                        else:
                            # there are more dialogues in rpl: needs process
                            replica_deconstruction_result = process_fin_replica_subreplicas(candidate_finish_prt_case_four)
                            if replica_deconstruction_result:
                                f_found_case_four = True
                                f_case_four = replica_deconstruction_result
                    elif s_found_case_four:
                        # divide fist time cases and multiply cases
                        if a_prt_case_four:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a,-d."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                        # the first time check
                        else:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a,-d."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                    else:
                        # start part still not found
                        if s_prt_case_four:
                            # check if the cerrent prt is an end of start part
                            if end_of_start_replica.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # D, d - direct speech, A,a - author speech
                                # replica_candidate_patterns = ["-D-d,-a.", "-D-d?-a.", "-D-d!-a.", "-D-d...-a."]
                            # check grammatically wrong but used by some authors puttern
                            elif dot_in_the_end.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d.-a."]
                            # If end of start replica still not found, then put current repl to s_prt_case_four
                            else:
                                s_prt_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d-d."]
            if s_found_case_four and a_found_case_four and f_found_case_four:
                # clean refined replica: change coma for dot between s & f parts
                dirty_s = s_case_four
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*-\s*[А-Я]", f_case_four):
                        sub_text = end_coma.sub(r".", dirty_s)
                        s_case_four = sub_text
                    if re.search(r"^\s*-\s*[а-я]", f_case_four):
                        sub_text = end_coma.sub(r",", dirty_s)
                        s_case_four = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*-\s*[а-я]", f_case_four):
                        tmp_list = []
                        sub_str = re.sub(r"\s*-\s*", " ", f_case_four)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        f_case_four = " ".join(tmp_list)
                refined_replica = s_case_four + " " + re.sub(r"\s*-\s*", " ", f_case_four)
            else:
                refined_replica = s_case_four

    # check for dash used
    if re.match(r"^[\s]*(—)[\s]*[А-ЯA-Z0-9]", raw_replica):
        # put a replica to tmp var for further processing
        tmp_replica: str = re.sub(r"\s+", " ", raw_replica)
        # prepare a list with hyphen positions <int> in the replica
        instring_position = []
        # populate the list with ints of start positions of hyphens met
        for m in dash.finditer(tmp_replica):
            instring_position.append(m.start())
        # length is a number of huphens found
        length = len(instring_position)
        # Case 1: -Здравствуйте! Я ваш сосед! / "-D.", "-D..." "-D!", "-D?"
        if length == 1:
            refined_replica = tmp_replica
            # refined replica returns: "-D"
        # Case 2: -Ай! - и бегом в сторону. / "-D,-a.", "-D?-a.", "-D!-a.", "-D...-a." or "-D-d."
        if length == 2:
            # tmp text is a part from first to start of second hyphen
            tmp_text_case_two: str = tmp_replica[instring_position[0]:instring_position[1]]
            # firstly process cases with Direct & Author speeches: grammatically right
            if end_of_start_replica.search(tmp_text_case_two):
                refined_replica = tmp_text_case_two
                # refined replica returns: "-D,", "-D?", "-D!", "-D..."
            # process cases with Direct & Author speeches: grammatically wrong
            elif dot_in_the_end.search(tmp_text_case_two):
                refined_replica = tmp_text_case_two
                # refined replica returns: "-D."
            else:
                # process cases with Direct speeches with hyphen in the middle
                if end_of_sentence.search(tmp_replica[instring_position[1]:]):
                    refined_replica = tmp_replica[instring_position[0]:]
                else:
                    refined_replica = tmp_replica[instring_position[0]:]
                    # refined replica returns: "-D-d.!?"
        # Case 3: -А что я могу сделать? - сказала она. - Я ни минуточки не могу посидеть спокойно, пока дела не сделаю.
        # "-D[,!?...][.]-a[.,]- D/d[.!?]", "—D[,!?...][.]—а.А[:.!?]—D." or "-D-d[,!?...][.]-a." or "-D[,!?...][.]-a-a." or "-D-d-d[.!?...]"
        if length == 3:
            # prepare vars for patterns search
            tmp_s_case_three: str = ''
            tmp_a_case_three: str = ''
            tmp_f_case_three: str = ''
            tmp_s_prt_case_three: str = ''
            tmp_a_prt_case_three: str = ''
            s_found_case_three: bool = False
            a_found_case_three: bool = False
            f_found_case_three: bool = False
            # loop trough hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                if n == 0:
                    # apparently the replica starts with direct speech: check for its boundaries
                    # check if start part coincide with first part of direct speech: grammatically right
                    if end_of_start_replica.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D[,!?...]"
                    # check if start part coincide with first part of direct speech: grammatically wrong
                    elif dot_in_the_end.search(tmp_replica[instring_position[0]:instring_position[1]]):
                        # if yes than we found start part
                        s_found_case_three = True
                        tmp_s_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                        # tmp_s_case_three returns: "-D."
                    # if not, then possible pattern is "-D-d[,!?...]-a."
                    else:
                        # put the first part in tmp var for use in the next step
                        tmp_s_prt_case_three = tmp_replica[instring_position[0]:instring_position[1]]
                if n == 1:
                    # on the second step firstly check the "start repl found" case
                    if s_found_case_three:
                        # check if current part is an author repl. Possible patterns: —а.А[:.!?] & -a[.,]
                        if dot_in_the_middle.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then possible patterns: —а.А[:.!?]
                            if end_of_author_speech_long.search(
                                    tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: —а.А[:.!?]
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                        # if no dot in the middle, then check for normal author speech pattern
                        else:
                            if end_of_author_speech.search(tmp_replica[instring_position[1]:instring_position[2]]):
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                                # tmp_a_case_three returns: "-a[.,]"
                            # if not, then possible pattern is "-D[,!?...]-a-a."
                            else:
                                # put the first part of author speech in tmp var for use in the next step
                                tmp_a_prt_case_three = tmp_replica[instring_position[1]:instring_position[2]]
                    # now check the "start repl not found" case
                    if s_found_case_three == False:
                        # check if current part is an end of grammatically right start repl
                        if end_of_start_replica.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes, then start repl found
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d[,!?...]"
                        # check if current part is an end of grammatically wrong start repl
                        elif dot_in_the_end.search(tmp_replica[instring_position[1]:instring_position[2]]):
                            # if yes than we found start part
                            s_found_case_three = True
                            # add the current part to the previous step found prt
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                      instring_position[1]:instring_position[2]]
                            # tmp_s_case_three returns: "-D-d."
                        # if not, then possible pattern is "-D-d-d[.!?...]"
                        else:
                            # put the first two parts in tmp var for use in the next step
                            tmp_s_prt_case_three = tmp_s_prt_case_three + tmp_replica[
                                                                          instring_position[1]:instring_position[2]]
                if n == 2:
                    # in the last step firstly check the "start repl found" & "author repl found" case
                    if s_found_case_three and a_found_case_three:
                        # apparently current part is a finish part
                        f_found_case_three = True
                        tmp_f_case_three = tmp_replica[instring_position[2]:]
                        # tmp_f_case_three returns: "- D/d[.!?]" or "-D."
                    # check the "start repl found" & "author repl not found" case
                    elif s_found_case_three:
                        # check for possible pattern "-D[,!?...]-a-a." or "-D-d[,!?...][.]-a."
                        if dot_in_the_end.search(tmp_replica[instring_position[2]:]):
                            # if yes we found author speech. Possible patterns: "-a-a."  or "-a."
                            if tmp_a_prt_case_three:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_a_prt_case_three + tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a-a."
                            else:
                                a_found_case_three = True
                                tmp_a_case_three = tmp_replica[instring_position[2]:]
                                # tmp_a_case_three returns: "-a."
                    # check the "start repl not found" case
                    elif s_found_case_three == False:
                        # check for possible pattern "-D-d-d[.!?...]"
                        if end_of_sentence.search(tmp_replica[instring_position[2]:]):
                            # if yes than we found full start repl
                            s_found_case_three = True
                            tmp_s_case_three = tmp_s_prt_case_three + tmp_replica[instring_position[2]:]
                            # tmp_s_case_three returns: "-D-d-d[.!?...]"
            # now let`s construct refined replica to return
            if s_found_case_three and a_found_case_three and f_found_case_three:
                # clean parts of replica: change coma for dot beetween s & f
                dirty_s = tmp_s_case_three
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*—\s*[А-Я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r".", dirty_s)
                        tmp_s_case_three = sub_text
                    elif re.search(r"^\s*—\s*[а-я]", tmp_f_case_three):
                        sub_text = end_coma.sub(r",", dirty_s)
                        tmp_s_case_three = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*—\s*[а-я]", tmp_f_case_three):
                        tmp_list = []
                        sub_str = re.sub(r"\s*—\s*", " ", tmp_f_case_three)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        tmp_f_case_three = " ".join(tmp_list)
                refined_replica = tmp_s_case_three + " " + re.sub(r"\s*-\s*", " ", tmp_f_case_three)
            else:
                refined_replica = tmp_s_case_three
        # case 4:-Ай-ай-ай! - и бегом в сторону.
        # unpredictable number of hyphens in a replica "-D-d-d, -a-a. -D-d-d-d. -a. -D. -A."
        if length > 3:
            # initiate vars
            s_case_four: str = ''
            a_case_four: str = ''
            f_case_four: str = ''
            s_prt_case_four: str = ''
            a_prt_case_four: str = ''
            f_prt_case_four: str = ''
            current_prt_case_four: str = ''
            # candidate_s_prt_case_four: str = ''
            candidate_finish_prt_case_four: str = ''
            replica_candidate_patterns: list = []
            s_found_case_four: bool = False
            a_found_case_four: bool = False
            f_found_case_four: bool = False
            # iterate through hyphens found in the replica and try to recognise parts divisions
            for n in range(length):
                # check the first occurance
                if n == 0:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[0]:instring_position[1]]
                    # check if the first part is a start repl: grammatically right
                    if end_of_start_replica.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # D, d - direct speech, A,a - author speech
                        # replica_candidate_patterns = ["-D,-a.", "-D?-a.", "-D!-a.", "-D...-a."]
                    # grammatically wrong but used by some authors pattern
                    elif dot_in_the_end.search(current_prt_case_four):
                        s_found_case_four = True
                        s_case_four = current_prt_case_four
                        # replica_candidate_patterns = ["-D.-a."]
                    else:
                        s_prt_case_four = current_prt_case_four
                # check last occurence
                elif n == length - 1:
                    current_prt_case_four = tmp_replica[instring_position[n]:]
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        break
                    elif s_found_case_four and a_found_case_four:
                        f_found_case_four = True
                        f_case_four = current_prt_case_four
                    elif s_found_case_four:
                        if a_prt_case_four:
                            a_found_case_four = True
                            a_case_four = a_prt_case_four + current_prt_case_four
                        else:
                            a_found_case_four = True
                            a_case_four = current_prt_case_four
                    else:
                        # end of replica start part still not found
                        if s_prt_case_four:
                            s_found_case_four = True
                            s_case_four = s_prt_case_four + current_prt_case_four
                        else:
                            s_found_case_four = True
                            s_case_four = current_prt_case_four
                else:
                    # put current part in separate var
                    current_prt_case_four = tmp_replica[instring_position[n]:instring_position[n + 1]]
                    # define current position in the vertual flow
                    if s_found_case_four and a_found_case_four and f_found_case_four:
                        continue
                    elif s_found_case_four and a_found_case_four:
                        # check if final part by chance enriched with dir spch & auth spch or not
                        candidate_finish_prt_case_four = tmp_replica[instring_position[n]:]
                        if last_replica_simple(candidate_finish_prt_case_four, dash):
                            # rpl is simple: just add
                            f_found_case_four = True
                            f_case_four = candidate_finish_prt_case_four
                        else:
                            # there are more dialogues in rpl: needs process
                            replica_deconstruction_result = process_fin_replica_subreplicas(
                                candidate_finish_prt_case_four)
                            if replica_deconstruction_result:
                                f_found_case_four = True
                                f_case_four = replica_deconstruction_result
                    elif s_found_case_four:
                        # divide fist time cases and multiply cases
                        if a_prt_case_four:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a,-d."]
                                else:
                                    a_prt_case_four = a_prt_case_four + current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                        # the first time check
                        else:
                            # check if current replica part is an author speech
                            if dot_in_the_middle.search(current_prt_case_four):
                                if end_of_author_speech_long.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a.A[.!?:]-D."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                            else:
                                if end_of_author_speech.search(current_prt_case_four):
                                    a_found_case_four = True
                                    a_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a,-d."]
                                else:
                                    a_prt_case_four = current_prt_case_four
                                    # D, d - direct speech, A,a - author speech
                                    # replica_candidate_patterns = ["-D[!...?,]-a-a[.,]-D."]
                    else:
                        # start part still not found
                        if s_prt_case_four:
                            # check if the cerrent prt is an end of start part
                            if end_of_start_replica.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # D, d - direct speech, A,a - author speech
                                # replica_candidate_patterns = ["-D-d,-a.", "-D-d?-a.", "-D-d!-a.", "-D-d...-a."]
                            # check grammatically wrong but used by some authors puttern
                            elif dot_in_the_end.search(current_prt_case_four):
                                s_found_case_four = True
                                s_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d.-a."]
                            # If end of start replica still not found, then put current repl to s_prt_case_four
                            else:
                                s_prt_case_four = s_prt_case_four + current_prt_case_four
                                # replica_candidate_patterns = ["-D-d-d."]
            if s_found_case_four and a_found_case_four and f_found_case_four:
                # clean refined replica: change coma for dot between s & f parts
                dirty_s = s_case_four
                if end_coma.search(dirty_s):
                    if re.search(r"^\s*—\s*[А-Я]", f_case_four):
                        sub_text = end_coma.sub(r".", dirty_s)
                        s_case_four = sub_text
                    if re.search(r"^\s*—\s*[а-я]", f_case_four):
                        sub_text = end_coma.sub(r",", dirty_s)
                        s_case_four = sub_text
                if end_of_sentence.search(dirty_s):
                    if re.search(r"^\s*—\s*[а-я]", f_case_four):
                        tmp_list = []
                        sub_str = re.sub(r"\s*—\s*", " ", f_case_four)
                        first_word_list = sub_str.split()
                        for i in range(len(first_word_list)):
                            if i == 0:
                                new = first_word_list[0]
                                tmp_list.append(new.title())
                            else:
                                tmp_list.append(first_word_list[i])
                        f_case_four = " ".join(tmp_list)
                refined_replica = s_case_four + " " + re.sub(r"\s*—\s*", " ", f_case_four)
            else:
                refined_replica = s_case_four
    # # clean refined replica: change coma for dot in the end of a sentence
    dirty_coma = refined_replica
    if end_coma.search(dirty_coma):
        sub_text = end_coma.sub(r".", dirty_coma)
        refined_replica = sub_text
    else:
        return refined_replica
    return refined_replica


# extract & save dialogues
def extract_n_save_replicas(src_path, dataset_path):
    source_files_paths: list = []
    dialogue_list: list = []
    # open dir with preprocessed file
    subdir_one: str = "automatically_created_copies_of_utf_encoded_files"
    subdir_two: str = "preprocessed_files"
    source_path_dir_tmp: str = os.path.join(src_path, subdir_one)
    source_path_dir: str = os.path.join(source_path_dir_tmp, subdir_two)
    for root, directories, files in os.walk(source_path_dir):
        for filename in files:
            filepath: str = os.path.join(root, filename)
            source_files_paths.append(filepath)
    counter = 1
    for path in source_files_paths:
        dataset_file_name: str = f"dataset_{str(counter)}.txt"
        dataset_file_path: str = os.path.join(dataset_path, dataset_file_name)
        with open(dataset_file_path, 'w', encoding='utf-8') as storage:
            with open(path, 'r', encoding='utf-8') as text:
                for line in text:
                    # finding of a replica
                    if line == r"\n\n":
                        continue
                    elif line == r"\n":
                        continue
                    elif line == r"\r":
                        continue
                    elif re.match(r"^\s*[-—]\s*[А-ЯA-Z0-9]", line):
                        # a possible dialogue line has been found
                        # delete possible parenthesis
                        if re.search(r"\([^)]*\)|\[[^]]*]|\{[^}]*}", line):
                            line = re.sub(r"\([^)]*\)|\[[^]]*]|\{[^}]*}", "", line)
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
        counter += 1
