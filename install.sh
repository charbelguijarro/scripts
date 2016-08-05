#!/usr/bin/env bash

target=/usr/local/bin/

sudo cp backup-dd.sh ${target}backup-dd
sudo cp check_chinese.py ${target}check_chinese
sudo cp irclog.sh ${target}irclog
sudo cp practice_chinese.py ${target}practice_chinese
sudo cp share_expenses.py ${target}share_expenses
sudo cp update-todolist.py ${target}update-todolist

sudo chmod 755 ${target}*

echo "Scripts have been installed"
