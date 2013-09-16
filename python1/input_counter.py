#!/usr/local/bin/python3
"""Analyzes user input and returns a list of words and their positions in the input"""

word_set = set([])
word_dict = dict()
uin = None

while uin != "":
    uin = input("Enter text: ")
    for punct in """`~!@#$%^&*()_-+={[}]|\:;"'<,>.?/""":
        uin = uin.replace(punct, "")
    words = uin.strip().split()
    for word in words:
        prev_set_length = len(word_set)
        word_set.add(word)
        if len(word_set) != prev_set_length:
            word_dict[word] = len(word_set)
    for word, length in word_dict.items():
        print(word, length)
else:
    print("Finished")
