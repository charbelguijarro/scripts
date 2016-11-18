#!/usr/bin/env python3
"""
    This script is used to update a personal diary with a specific syntax. 
    This is how I'm written my own personal diary : 
    # Vendredi 18 Novembre - 25.24374894
    Aujourd'hui, j'ai fait telle chose importante, et j'ai pensé à cette fameuse idée.
    C'était une bonne journée.

    # Jeudi 17 Novembre - 25.23871146
    Journée pluvieuse, comme mon esprit et mon âme....

    This script automatize the writing of the first line. It writes the actual date, 
    and display your exact age based on my personal script age_counter.py. 
"""

from datetime import date
import datetime as dt
import age_counter

# Personal constants variables
JOURNAL = '/home/nairwolf/Documents/misc/diary/journal.md'
BIRTHDAY = '21/08/1991 - 19h30'

# Locale variables
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
    """
        Open the file located at 'filepath' and stores the text in the 
        variable 'content' and returns it.
    """
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def update_text(content):
    """
        Take the content inside the diary file, and update the first line if 
        needed. If the first line doesn't correspond with the actual date, 
        this function update the variable 'content' with the actual date at 
        the beginning. Moreover, it adds a timestamp which is your precise
        age computed by an other script. 
    """
    actual_date = get_actual_date()
    first_line = content.splitlines()[0]
    date_on_file = first_line.split(' - ')[0]
    
    if actual_date != date_on_file: # dates are different 
        age = str(age_counter.counter(from_date=BIRTHDAY))
        content = actual_date + ' - ' + age + '\n\n' + content

    return content

def get_actual_date():
    """
        Compute the actual date and returns it 
        with this format : '# Vendredi 18 Novembre'
    """
    today = dt.date.today()
    weekday = DAYS[today.isoweekday() - 1]
    daynumber = today.day
    month = MONTHS[today.month - 1]

    return '# {} {} {}'.format(weekday, daynumber, month)

def write_content(filepath, content):
    """
        Open the file located at 'filepath' and write the string 
        variable 'content' inside.
    """
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
