#!/usr/local/bin/python3
"""Loops over a list of tuples, using string formatting to display data"""

data = ((1,1),(2,2),(12,13),(4,4),(99,98))

for x, y in data:
    print("{0:>4} = {1:2} x {2:2}".format(x*y, x, y))
