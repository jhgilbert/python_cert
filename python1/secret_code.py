#!/usr/local/bin/python3
'''Convert user input to secret code'''

uin = input("Message: ")
newstring = ""
for c in reversed(uin):
    newstring += chr(ord(c) + 1)
print(newstring)
