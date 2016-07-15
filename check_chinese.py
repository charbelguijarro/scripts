#!/usr/bin/env python3
import sys
import os

def sanitize(line, exception):
    if line.startswith(exception) == False:
        line = '* ' + line
    return line

if __name__ == "__main__":
    filename = sys.argv[1]
    tmp_file = filename+'_tmp'
    exception = ('#', '\n', '*')
    with open(filename, 'r') as fi:
        lines = ""
        for line in fi:
            line = sanitize(line, exception)
            lines += line

    with open(tmp_file, 'w') as fo:
        fo.write(lines)

    os.rename(tmp_file, filename)
    print("file has been written")
