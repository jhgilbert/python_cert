#!/usr/local/bin/python3
'''Game in which the user tries to guess a number'''
from random import randint
secret = randint(1,20)
uin = 0
guesses = 0
while guesses < 5:
    uin = int(input("Guess a number: "))
    if uin == secret:
        print("Correct! Well done, the number was", secret)
        break
    elif uin < secret:
        print("Guess higher")
        guesses += 1
    elif uin > secret:
        print("Guess lower")
        guesses += 1
else:
    print("Sorry, the number was", secret)

