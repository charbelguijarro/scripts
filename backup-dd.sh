#!/bin/bash

backup_date=$(date +%Y%m%d)
src_dirs=("/data" "/home/nairwolf")
dest=/media/nairwolf/b770cf56-f1e0-45ce-a608-5f1a0a56cfeb/backup/
exclude_args=--exclude='nairwolf/.cache/'

if [ ! -d "$dest" ]
then
	echo "The back up hard drive is not present"
	exit 1
fi

for src in "${src_dirs[@]}"
do
	echo "**************"
	echo "Back up the repository : '$src'"
	name_src=$(basename $src)
	backup_report="$dest"backup-"$name_src"-"$backup_date"
	touch "$backup_report" 

	if [ ! -f "$backup_report" ]
	then
		echo "$backup_report can't be created"
		exit 1
	fi

	rsync -a -v --delete --stats "$exclude_args" "$src" "$dest" > "$backup_report"

	if [ "$?" -eq 0 ]
	then
		echo "Back up done with success"
	else
		echo "Back up has failed"
		exit 1
	fi

done
echo "**************"
echo ""
echo "Back up finished"
