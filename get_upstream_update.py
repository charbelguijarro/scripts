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
    update:
        vim/zesty 2:7.5.1829-1ubuntu3 amd64 [upgradable from: 2:7.4.1829-1ubuntu2]
    """    

    text = text.strip()
    pattern_version = re.compile(r'(\d+\.\d+\.\d+)')
    pattern_package_name = re.compile(r'(.*)/')
    for line in text.splitlines():
        line = line.strip()
        version = pattern_version.findall(line)
        if len(version) == 2:
            if version[0] != version[1]:
                package_name = pattern_package_name.findall(line)[0]
                print("'{}' has an upstream update: {} -> {}".format(package_name, 
                                                                     version[1],
                                                                     version[0]))
if __name__ == '__main__':
    text = sys.stdin.read()
    get_upstream_update(text)
