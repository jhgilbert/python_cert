#!/usr/local/bin/python3

import random
n = random.randint(1, 99)

while True:
    uin = int(input("Guess a number: "))
    if uin < n:
        print("Too low")
    elif uin > n:
        print("Too high")
    else:
        print("You guessed it!")
        break
