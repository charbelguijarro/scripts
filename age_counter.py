#!/usr/bin/env python3

import datetime as dt
from argparse import ArgumentParser

def parse_date(date):
    """
        Returns date in struct_time object
    """
    try:
        date = dt.datetime.strptime(date, '%d/%m/%Y - %Hh%M')
    except ValueError:
        try:
            date = dt.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            print("The format's date used is not correct")

    return date

def get_diff(from_date, to_date):
    """
        compute age and time_diff between two dates. 
        age <int> : difference in year between the two dates.
        time_diff <datetime.timedelta> : difference the last birthday and now.
    """
    birthday = dt.datetime(to_date.year, from_date.month, from_date.day, 
                            from_date.hour, from_date.minute)
    last_birthday = birthday

    age = birthday.year - from_date.year

    if (to_date.month, to_date.day) < (birthday.month, birthday.day):
        age -= 1
        last_birthday = dt.datetime(now.year - 1, born.month, born.day)

    time_diff = to_date - last_birthday

    return age, time_diff
    
def compute_age(age, diff):
    one_year = 365.24219879 
    one_day = 24 * 60 * 60
    one_year_secs = one_day * one_year

    diff_secs = diff.total_seconds()
    age_deci = diff_secs / one_year_secs

    final_age = round(age + age_deci, 8)

    return final_age

def counter(from_date='1/1/1970', to_date=None):
    """
        Takes two dates and compute precisely the difference in 
        years between these two dates. 
        If from_date='1/1/2000' and to_date='1/2/2001' the output
        will be 1.08487518 (one year + one month)
    """
    from_date = parse_date(from_date)
    if not to_date:
        to_date = dt.datetime.now() 
    else:
        to_date = parse_date(to_date)
    age, time_diff = get_diff(from_date, to_date)
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
    age = counter(args.from_date, args.to_date)
    print("You have {} years old!".format(age))
