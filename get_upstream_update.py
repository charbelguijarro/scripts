#!/usr/bin/env python3

import re
import sys

def get_upstream_update(text):
    """
    Take the output of the command `apt list --upgradable and returns
    only upstream_updates
    text: 
        vim/zesty 2:7.5.1829-1ubuntu3 amd64 [upgradable from: 2:7.4.1829-1ubuntu2]
        vim-common/zesty 2:7.4.1829-1ubuntu3 amd64 [upgradable from: 2:7.4.1829-1ubuntu2]
        mysql-common/zesty,zesty 5.8+1.0.0ubuntu1 all [upgradable from: 5.7.15-0ubuntu2]
    update:
        'vim' has an upstream update: 7.4.1829 -> 7.5.1829
        'mysql-common' has an upstream update: 5.7.15 -> 5.8
    """    

    text = text.strip()
    pattern_version = re.compile(r'(\d+\.\d+(\.\d+)?)')
    pattern_package_name = re.compile(r'(.*)/')
    for line in text.splitlines():
        line = line.strip()
        versions = pattern_version.findall(line)
        # versions = [('5.8', ''), ('1.0.0', '.0'), ('5.7.15', '.15')]
        new = versions[0][0]
        old = versions[-1][0]
        if new != old:
            package_name = pattern_package_name.findall(line)[0]
            print("'{}' has an upstream update: {} -> {}".format(package_name, 
                                                                     old, new))
if __name__ == '__main__':
    text = sys.stdin.read()
    get_upstream_update(text)
