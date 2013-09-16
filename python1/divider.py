#!/usr/local/bin/python3
""" Practice handling exceptions """

while True:
    uin = input("Provide an integer: ")
    if not uin:
        break
    try:
        result = 10/int(uin)
        print(result)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")
    