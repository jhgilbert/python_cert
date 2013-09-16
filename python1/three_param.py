#!/usr/local/bin/python3

def my_func(a, b='b was not entered', c='c was not entered'):
    """Prints the value of up to three strings"""
    print(a)
    print(b)
    print(c)

str1 = "test"

my_func(str1)
my_func(str1, str1)
my_func(str1, str1, str1)
print(my_func)
