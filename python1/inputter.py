#!/usr/local/bin/python3
'''Takes input from the user and saves it to a file'''

f = open('text_from_user.txt', 'a')
f.close()
f = open('text_from_user.txt','r')
print(f.read())
while True:
    uin = input("Enter text: ")
    if uin == "":
        break
    f = open('text_from_user.txt','a')
    f.write(uin)
    f.close()
    f = open('text_from_user.txt', 'r')
    print(f.read())
    f.close()

