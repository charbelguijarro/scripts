#!/usr/bin/env python3

from datetime import date

JOURNAL = '/home/nairwolf/Documents/misc/diary/journal.md'
DAYS = ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')
MONTHS = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', \
        'Septembre', 'Octobre', 'Novembre', 'Décembre')

def main():
    content = get_content(JOURNAL)
    content = add_current_day(content)
    write_content(JOURNAL, content)

def get_content(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def add_current_day(content):
    today = date.today()
    weekday = DAYS[today.isoweekday() - 1]
    daynumber = today.day
    month = MONTHS[today.month - 1]

    datestring = '# {} {} {}\n\n'.format(weekday, daynumber, month)

    content = datestring + content
    return content

def write_content(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
