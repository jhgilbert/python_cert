#!/usr/local/bin/python3
"""Makes lists of words from a user's text"""

uin = input("Input your text: ")
for punct in """`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?""":
    uin = uin.replace(punct, "")
all_words = uin.strip().split()
capped_words = []
lc_words = []

for word in all_words:
    if word.lower() != word:
        capped_words.append(word)
    else:
        lc_words.append(word)

for word in (capped_words + lc_words):
    print(word)

