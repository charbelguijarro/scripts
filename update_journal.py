#!/usr/bin/env python3

from datetime import date
import age_counter

JOURNAL = '/home/nairwolf/Documents/misc/diary/journal.md'
DAYS = ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')
MONTHS = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', \
        'Septembre', 'Octobre', 'Novembre', 'Décembre')

def main():
    content = get_content(JOURNAL)
    content = update_text(content)
    write_content(JOURNAL, content)

def get_content(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def update_text(content):
    actual_date = get_actual_date()
    first_line = content.splitlines()[0]
    date_on_file = first_line.split('-')[0]
    
    if actual_date != date_on_file: 
        age = str(age_counter.counter())
        content = actual_date + ' - ' + age + '\n\n' + content

    

    return content

def get_actual_date():
    today = date.today()
    weekday = DAYS[today.isoweekday() - 1]
    daynumber = today.day
    month = MONTHS[today.month - 1]

    return '# {} {} {}'.format(weekday, daynumber, month)

def write_content(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
