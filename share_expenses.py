#!/usr/bin/env python3
import sys

def print_difference(account):
    valueF = account["F"]
    valueJ = account["J"]
    total = valueF + valueJ

    print("Dépense Florian : "+str(valueF)+"€")
    print("Dépense Junyi : "+str(valueJ)+"€")
    print("Dépense totale : "+str(total)+"€")
    print("==========================")

    if valueF < valueJ:
        diff = round((valueJ - valueF)/2, 2)
        print("Florian doit "+str(diff)+"€ à Junyi.")
    elif valueJ < valueF:
        diff = round((valueF - valueJ)/2, 2)
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
        value = float(expense[1])
        account = add_expense(account, name, value)
    print_difference(account)

