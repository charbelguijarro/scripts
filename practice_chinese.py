#!/usr/bin/env python3

import sys, os
import random

def get_chinese_words(line):
    word_list = []
    if line.startswith('*'):
        line = line.replace('*', '')
        for sentence in line.split(':'):
            word = sentence.strip().rstrip()
            word_list.append(word)
    return word_list

def pick_a_word(chinese_words):
    word = random.choice(chinese_words)
    wtype = random.randint(0, 1)

    # We suppose wtype == 0
    target = "{} ({})".format(word[0], word[1])
    solution = word[2]

    if wtype == 1:
        target, solution = solution, target

    return target, solution

def create_line_word(target, solution):
    if "(" in solution:
        target, solution = solution, target

    target = target.replace('(', ': ').replace(')', '')
    wordline = "* "+target+" : "+solution

    return wordline

def write_errors_file(failed_words):
    with open('errors.md', 'a') as f:
        for wordline in failed_words:
            f.write(wordline+'\n')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Enter filename as argument")
        exit()

    if not os.path.exists(filename):
        print("Enter existing filename")
        exit()

    chinese_words = []
    failed_words = []

    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            word_list = get_chinese_words(line)
            if word_list:
                chinese_words.append(word_list)

    while True:
        nb = input("How many times do you want to play ?\n")
        try:
            nb = int(nb)
        except ValueError:
            print("Enter a positive value !")
            continue
        if nb >= 0:
            break
        else:
            print("Enter a positive value !")
            continue
        

    nb_success = 0

    for i in range(0, int(nb)):
        print("****************************")
        print("Exercice n°{}".format(i+1))

        target, solution = pick_a_word(chinese_words)

        input('What does this word mean "{}" ?\n'.format(target))
        print('The solution is "{}"'.format(solution))

        while True:
            rst = input("Is it correct ? (y/n) ")
            if rst in ('y', 'n'):
                if rst == 'y':
                    nb_success += 1
                else:
                    words = create_line_word(target, solution)
                    failed_words.append(words)
                break
            else:
                print("'{}' isn't a correct answer".format(rst))
                continue

        percentage = round((nb_success / (i+1))*100)
        print("****************************")
        print("Good answers : {}/{}".format(nb_success, nb))
        print("Success rate : {}%".format(percentage))
        
    if filename != 'errors.md':
        write_errors_file(failed_words)
