#!/usr/bin/env python3
import sys

def print_difference(account):
    valueF = account["F"]
    valueJ = account["J"]

    if valueF < valueJ:
        diff = valueJ - valueF
        print("Florian doit "+str(diff)+"€ à Junyi.")
    elif valueJ < valueF:
        diff = valueF - valueJ
        print("Junyi doit "+str(diff)+"€ à Florian.")
    else:
        print("Égalité.")

def add_expense(account, name, value):
    if name == "F":
        account["F"] += value
    else:
        account["J"] += value

    return account

if __name__ == "__main__":
    account = {"F":0, "J":0}
    lines = sys.stdin.readlines()
    for l in lines:
        expense = l.split()
        name = expense[0]
        value = int(expense[1])
        account = add_expense(account, name, value)
    print_difference(account)

