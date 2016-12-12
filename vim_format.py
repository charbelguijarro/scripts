#!/usr/bin/env python3

import sys
import textwrap

WIDTH_MAX = 80

def add_carriage_return(content):
    lines = []
    for line in content.splitlines():
        newline = line
        if line.startswith('#'):
            newline = line + '\n' 
        lines.append(newline)

    return '\n'.join(lines)

def remove_carriage_return(content):
    lines = content.splitlines()
    new_lines = [v for i, v in enumerate(lines) 
                    if i == 0 or not lines[i-1].startswith('#')]
    
    """
    lines = iter(content.splitlines())
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.startswith('#'):
            next(lines, False)

    """
    return '\n'.join(new_lines)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1] 
    else:
        print("Enter an existing filename")
        exit()

    with open(filename, 'r') as fi:
        content = fi.read()

    content = add_carriage_return(content)

    paragraphs = content.split('\n\n')

    wrapped_content = ''
    for paragraph in paragraphs:
        new_pr = textwrap.fill(paragraph, width=WIDTH_MAX) + '\n\n'
        wrapped_content += new_pr

    new_content = remove_carriage_return(wrapped_content)

    with open(filename, 'w') as fo:
        fo.write(new_content.strip())
