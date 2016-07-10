#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    md_file = sys.argv[1]

    mdf = open(md_file)
    new_mdf = open("new_"+md_file, 'w')
    exception = ('#', '\n')


    for line in mdf:
        if line.startswith(exception) == False:
            line = '* ' + line
        new_mdf.write(line)


    mdf.close()
    new_mdf.close()
