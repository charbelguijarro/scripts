#!/bin/bash

BACKUP_DATE=$(date +%Y%m%d)
SRC=("/data" "/home/nairwolf")
DEST=/media/nairwolf/b770cf56-f1e0-45ce-a608-5f1a0a56cfeb/backup/

if [ ! -d "$DEST" ]
then
	echo "The back up hard drive is not present"
	exit 1
fi

for src in "${SRC[@]}"
do
	echo "**************"
	echo "Back up the repository : '$src'"
	NAME_SRC=$(basename $src)
	BACKUP_REPORT="$DEST"backup-"$NAME_SRC"-"$BACKUP_DATE"
	touch "$BACKUP_REPORT" 

	if [ ! -f "$BACKUP_REPORT" ]
	then
		echo "$BACKUP_REPORT can't be created"
		exit 1
	fi

	rsync -a -v --delete --stats "$src" "$DEST" > "$BACKUP_REPORT"

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
