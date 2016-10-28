#!/usr/bin/env python3

import datetime as dt

# BIRTHDAY = 'dd/mm/yyyy - Hhm'
BIRTHDAY = '21/08/1991 - 19h30'

def parse_birthday():
    """
        Returns birthday in struct_time object
    """
    birthday = dt.datetime.strptime(BIRTHDAY, '%d/%m/%Y - %Hh%M')
    return birthday

def get_diff(born):
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

if __name__ == '__main__':
    age = counter()
    print("You have {} years old!".format(age))

