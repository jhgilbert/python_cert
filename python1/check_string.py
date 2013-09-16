#
# check_string.py
#
'''Tests to make sure that a string is all in upper case and ends with a period.'''
uin = input("Please enter an upper-case string ending with a period: ")
if uin.isupper() and uin.endswith("."):
    print("Input meets both requirements.")
elif uin.isupper():
    print("Input does not end with a period.")
elif uin.endswith("."):
    print("Input is not all upper case.")
else:
    print("Input does not end with a period and is not all upper case.")

