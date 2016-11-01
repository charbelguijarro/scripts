#!/usr/bin/env python3

from datetime import date
import datetime as dt
import age_counter

JOURNAL = '/home/nairwolf/Documents/misc/diary/journal.md'
DAYS = ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')
MONTHS = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', \
        'Septembre', 'Octobre', 'Novembre', 'Décembre')

def main():
    content = get_content(JOURNAL)
    content = update_text(content)
    content = verify_timestamp(content)
    write_content(JOURNAL, content)

def verify_timestamp(content):
    for line in content.splitlines():
        if line and line[0] == '#':
            line_split = line.split(' - ')
            if len(line_split) == 1:
                date = convert_string_date(line)
    return content

def convert_string_date(date):
    """
        date is '# Vendredi 1 Janvier', converts this string into 
        '01/01/2016 - 12h00'
    """
    date_list = date.split()
    day = date_list[2]
    month = date_list[3]

    format_date = "{}/{}/2016 - 12h00".format(day, month)
    return format_date


def get_content(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def update_text(content):
    actual_date = get_actual_date()
    first_line = content.splitlines()[0]
    date_on_file = first_line.split(' - ')[0]
    
    if actual_date != date_on_file: # dates are different 
        age = str(age_counter.counter())
        content = actual_date + ' - ' + age + '\n\n' + content

    return content

def get_actual_date():
    today = dt.date.today()
    weekday = DAYS[today.isoweekday() - 1]
    daynumber = today.day
    month = MONTHS[today.month - 1]

    return '# {} {} {}'.format(weekday, daynumber, month)

def write_content(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
