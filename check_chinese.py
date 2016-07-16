#!/usr/bin/env python3
import sys
import os

def collect_words(line, chinese_dict, line_nb):
    for word in line.split():
        # word can be '(wo3' or 'zou4)'
        # remove uncessary parens
        if word.startswith('('):
            word = word[1:]
        if word.endswith(')'):
            word = word[:-1]

        if word[-1].isdigit():
            accent = word[-1]
            word = word[:-1] 

            if word not in chinese_dict:
                chinese_dict[word] = [{line_nb}, {accent}]
            else:
                word_list = chinese_dict[word]
                word_list[0].add(line_nb)
                word_list[1].add(accent)

    return chinese_dict

def check_chinese_dict(d):
    for word, accents in d.items():
        if len(accents[1]) > 1:
            print("\nVérifiez le mot '"+ word +"' aux lignes suivantes:")
            for i in accents[0]:
                print(i)

def sanitize(line, exception):
    if line.startswith(exception) == False:
        line = '* ' + line
    line = line.replace('(', '- ').replace(')', ' ').replace(':', '-')
    return line

if __name__ == "__main__":
    filename = sys.argv[1]
    tmp_file = filename+'_tmp'
    exception = ('#', '\n', '*')
    chinese_dict = {}
    line_nb = 1

    with open(filename, 'r') as fi:
        lines = ""
        for line in fi:
            line = sanitize(line, exception)
            chinese_dict = collect_words(line, chinese_dict, line_nb)
            lines += line
            line_nb += 1

    with open(tmp_file, 'w') as fo:
        fo.write(lines)

    os.rename(tmp_file, filename)
    print("file has been written")
    check_chinese_dict(chinese_dict)
