#!/bin/bash

prefix="/.weechat/logs/irc.freenode."
suffix=".weechatlog"
arg="$1"
file=${HOME}${prefix}${arg}${suffix}

# Check input argument
if [[ $# -eq 0 ]]; then
	echo "no irc chan given"
	exit 1
fi

# Check if chan needs a '#' or not
if [[ ! -e "$file" ]]; then
	file=${HOME}${prefix}'#'${arg}${suffix}
fi

# Check if the file exists and read it !
if [[ ! -e "$file" ]]; then
	echo "This file '$file' doesn't exist"
	exit 1
else
	less "$file"
fi
