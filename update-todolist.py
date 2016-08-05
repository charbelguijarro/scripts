#!/usr/bin/env python3

import argparse
import os
from datetime import date, timedelta

"""
    todo-update
    Python script to automatize my personal todo list
"""

TODOLIST = 'todolist.md'
README = 'README.md'

def count_finished_tasks(lines):
    tasks = []
    for line in lines[2:]:
        if line.startswith('*'):
            tasks.append(line)
        elif line.startswith('##'):
            break

    nb_tasks = len(tasks)
    finished_tasks = len([task for task in tasks if 'FAIT' in task])
    percentage = (finished_tasks / nb_tasks) * 100

    return round(percentage)

def get_week():
    today = date.today()
    week_number = today.isocalendar()[1]
    start_week = today + timedelta(days=today.day - 1)
    end_week = start_week + timedelta(days=6)

    return week_number, start_week, end_week

def get_week_line():
    week_nb, start_week, end_week = get_week()
    line_to_print = "## Week {} - {}/{} -> {}/{}\n\n".format(week_nb, start_week.day, 
                                                            start_week.month,
                                                            end_week.day,
                                                            end_week.month)
    return line_to_print

def get_week_summary(percentage):
    week_nb, start, end = get_week()

    url = "https://gitlab.com/Nairwolf/ToDoList/blob/master/todolist.md"
    week_summary = "* [Week {}](".format(week_nb)
    
    week_summary += url+"#week-{}-{}-{}{}-{}{})".format(week_nb, week_nb, 
                                                        start.day, start.month,
                                                        end.day, end.month)

    week_summary += " : {}%\n".format(percentage)
    return week_summary

def update_todolist():
    with open(TODOLIST, 'r') as f:
        lines = f.readlines()

    percentage = count_finished_tasks(lines)

    new_week = get_week_line()
    if lines[1].rstrip() != new_week.rstrip():
        lines[0] += new_week

    with open(TODOLIST, 'w') as f:
        f.write(''.join(lines))

    return percentage

def update_readme(percentage):
    with open(README, 'r') as f:
        lines = f.readlines()

    week_summary = get_week_summary(percentage)
    if lines[4].rstrip() != week_summary.rstrip():
        lines[3] += week_summary

    with open(README, 'w') as f:
        f.write(''.join(lines))

def check_input():
    if not os.path.isfile(TODOLIST):
        print("Error: '{}' is not found".format(TODOLIST))
        quit()

    if not os.path.isfile(README):
        print("Error: '{}' is not found".format(README))
        quit()

if __name__ == '__main__':
    check_input()

    percentage = update_todolist()
    update_readme(percentage)
