#!/usr/local/bin/python3
"""Defines the Dog class"""

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

if __name__ == "__main__":
    dogs = []
    while True:
        iname = input("Enter a name: ")
        if not iname:
            break
        ibreed = input("Enter a breed: ")
        this_dog = Dog(iname, ibreed)
        dogs.append(this_dog)
        print('DOGS')
        print('*' * 25)
        for i, d in enumerate(dogs):
            print("{0}. {1}: {2}".format(i, d.name, d.breed))
        print('*' * 25)

