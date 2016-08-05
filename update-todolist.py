#!/usr/bin/env python3

import argparse
from datetime import date, timedelta

"""
    todo-update
    Python script to automatize my personal todo list
"""

def get_week_line():
    today = date.today()
    week = today.isocalendar()[1]
    start_week = today + timedelta(days=today.day - 1)
    end_week = start_week + timedelta(days=6)

    line_to_print = "## Week {} - {}/{} -> {}/{}\n\n".format(week, start_week.day, 
                                                            start_week.month,
                                                            end_week.day,
                                                            end_week.month)
    return line_to_print

def parse_args():
    """
        Parse args with argparse
    """
    parser = argparse.ArgumentParser(description='Create new paragraph for your own todolist')
    parser.add_argument('todolist')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    with open(args.todolist, 'r') as f:
        lines = f.readlines()

    new_week = get_week_line()
    if lines[1].rstrip() != new_week.rstrip():
        lines[0] += new_week
        #lines[1] = new_week + lines[1]

    with open(args.todolist, 'w') as f:
        f.write(''.join(lines))
