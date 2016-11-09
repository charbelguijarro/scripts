#!/usr/bin/env python3

import re
import sys

def _cmp(expected, result):
    """ 
        Returns True if expected == result
        else returns False
    """
    if expected == result:
        print("OK")
    else:
        print("FAIL")
        minlen = min(len(result), len(expected))
        for i in range(minlen):
            if result[i] != expected[i]:
                before = max(0, i-10)
                after = min(minlen, i+50)
                print("**********")
                print("Should be: {}\nIs: {}".format(expected[before:], result[before:]))
                break


def get_upstream_update(text):
    """
    Take the output of the command `apt list --upgradable and returns
    a list of upstream update
    text: 
        vim/zesty 2:7.5.1829-1ubuntu3 amd64 [upgradable from: 2:7.4.1829-1ubuntu2]
        vim-common/zesty 2:7.4.1829-1ubuntu3 amd64 [upgradable from: 2:7.4.1829-1ubuntu2]
        mysql-common/zesty 5.8+1.0.0ubuntu1 all [upgradable from: 5.7.15-0ubuntu2]
        xfce4-terminal/zesty 0.8.1-1 amd64 [upgradable from: 0.6.3-2ubuntu1]
    update:
        'xfce4-terminal' : 0.6.3 -> 0.8.1
    """    
    upstream = []
    text = text.strip()
    pattern = (r'(.+)/\w+ (\d+\.\d+(?:\.\d+)?).* (?:amd64|i386) \[upgradable from: '
               r'(\d+\.\d+(?:\.\d+)?).*')
    pattern_version = re.compile(pattern)

    for line in text.splitlines():
        line = line.strip()
        groups = pattern_version.findall(line)
        # groups = [('xfce4-terminal', '0.8.1', '0.6.3')]
        if groups and len(groups[0]) == 3:
            rst = groups[0]
            package_name = rst[0]
            new = rst[1]
            old = rst[2]
            if new != old:
                upstream.append("'{}' : {} -> {}".format(package_name, old, new))
    return upstream

if __name__ == '__main__':
    try:
        sys.argv[1] == 'DEBUG'
        text = """
            mysql-common/zesty 5.8+1.0.0ubuntu1 all [upgradable from: 5.7.15-0ubuntu2]
            xfce4-terminal/zesty 0.8.1-1 amd64 [upgradable from: 0.6.3-2ubuntu1]
            """
        rst = "\n".join(get_upstream_update(text))
        expected = """
'mysql-common' : 5.7.15 -> 5.8
'xfce4-terminal' : 0.6.3 -> 0.8.1"""
        _cmp(expected, rst)
    except:
        text = sys.stdin.read()
        print("\n".join(get_upstream_update(text)))

