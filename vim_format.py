#!/usr/bin/env python3

import sys
import textwrap

WIDTH_MAX = 90

def check_line(line):
    rst = []
    if len(line) <= WIDTH_MAX:
        return [line]
    else:
        i = line.rfind(' ', 0, WIDTH_MAX)
        l1 = line[:i]
        rest_line = line[i+1:]
        return [l1] + check_line(rest_line)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1] 
    else:
        print("Enter an existing filename")
        exit()

    with open(filename, 'r') as fi:
        contents = fi.read()

    paragraphs = contents.split('\n\n')

    new_content = ''
    for pr in paragraphs:
        lines = textwrap.fill(pr, width=WIDTH_MAX) + '\n\n'
        new_content += lines

    with open(filename, 'w') as fo:
        fo.write(new_content.strip())
