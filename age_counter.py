#!/usr/bin/env python3

import datetime as dt
from argparse import ArgumentParser

# BIRTHDAY = 'dd/mm/yyyy - Hhm'
BIRTHDAY = '21/08/1991 - 19h30'

def parse_birthday():
    """
        Returns birthday in struct_time object
    """
    birthday = dt.datetime.strptime(BIRTHDAY, '%d/%m/%Y - %Hh%M')
    return birthday

def get_diff(born):
    """
        compute age and time_diff between two dates. 
        age <int> : difference in year between the two dates.
        time_diff <datetime.timedelta> : difference the last birthday and now.
    """
    now = dt.datetime.now()
    birthday = dt.datetime(now.year, born.month, born.day, born.hour, born.minute)
    last_birthday = birthday

    age = birthday.year - born.year

    if (now.month, now.day) < (birthday.month, birthday.day):
        age -= 1
        last_birthday = dt.datetime(now.year - 1, born.month, born.day)

    time_diff = now - last_birthday

    return age, time_diff
    
def compute_age(age, diff):
    one_year = 365.24219879 
    one_day = 24 * 60 * 60
    one_year_secs = one_day * one_year

    diff_secs = diff.total_seconds()
    age_deci = diff_secs / one_year_secs

    final_age = round(age + age_deci, 8)

    return final_age

def counter():
    birthday = parse_birthday()
    age, time_diff = get_diff(birthday)
    precise_age = compute_age(age, time_diff)
    return precise_age

def _parse_args():
    parser = ArgumentParser(description='Compute precisely time between \
    two dates, displayed in years.')

    parser.add_argument('-f', 
            dest='from_date',
            default='1/1/1970',
            help="The date 'from' with this syntax : '1/12/2000'",
            metavar='date'
            )

    parser.add_argument('-t', 
            dest='to_date',
            help="The date 'to' with this syntax : '1/12/2000'",
            metavar='date',
            )

    return parser.parse_args()

if __name__ == '__main__':
    args = _parse_args()
    age = counter()
    print("You have {} years old!".format(age))

