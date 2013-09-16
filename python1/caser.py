#!/usr/local/bin/python3
import sys

def exit(str1):
    """Exits the program."""
    print("Quitting the program ...")
    sys.exit()

switch = {
    'capitalize': str.capitalize,
    'title': str.title,
    'upper': str.upper,
    'lower': str.lower,
    'exit': exit
    }

while True:
    chosen_func = input("Enter a function name: ({0}) ".format(", ".join(switch.keys())))
    uin = input("Enter a string: ")
    option = switch.get(chosen_func, None)
    if option:
        print(option(uin))
    else:
        print("Please choose a valid option!")
