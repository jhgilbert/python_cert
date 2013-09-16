#!/usr/local/bin/python3
""" Prints a histogram showing a word count for each of the word lengths encountered. """
import math

def split_file_into_words(filename):
    """ Splits a file into words and returns them in a list.
    >>> len(split_file_into_words("declaration.txt"))
    1322
    """
    f = open(filename, 'r')
    words = []
    for line in f.readlines():
        for word in line.split():
            words.append(word)
    f.close()
    return words


def measure_word_length(word):
    """ Measures the length of a word without punctuation marks.

    >>> measure_word_length("&there!")
    5
    >>> measure_word_length("Hi?")
    2
    """
    punctuation = ('!','@','#','$','%','^','&','*','(',')','-','+','-','=','[',']','{','}','\\','|',';',"'",':','"',',','.','/','<','>','?')
    wlength = 0
    for c in word:
        if c in punctuation:
           pass
        else:
            wlength += 1
    return wlength


def create_word_length_dict(filename):
    """ Builds a dictionary of word lengths.

    >>> create_word_length_dict("declaration.txt")
    {1: 16, 2: 267, 3: 267, 4: 169, 5: 140, 6: 112, 7: 99, 8: 68, 9: 61, 10: 56, 11: 35, 12: 13, 13: 9, 14: 7, 15: 2}
    """
    lengths = {}
    words = split_file_into_words(filename)
    # Tally word lengths
    for word in words:
       wlength = measure_word_length(word)
       current_entry = lengths.get(wlength, None)
       if current_entry:
           lengths[wlength] += 1
       else:
           lengths[wlength] = 1
    # Disregard words of zero length
    zero_count = lengths.get(0, None)
    if zero_count:
        del lengths[0]
    return lengths


def round_up(x):
    """ Rounds an integer up to the nearest ten or hundred.

    >>> round_up(11)
    20
    >>> round_up(313)
    400
    """
    if len(str(x)) <= 2:
        result = int(math.ceil(x/10.0)) * 10
    else:
        result = int(math.ceil(x/100.00)) * 100
    return result


def set_printed_y_values(x):
    """ Populates the numbers printed on the y axis of the histogram.

    >>> set_printed_y_values(14)
    [5, 10, 15, 20]
    """
    # set minimum high y value
    x = round_up(x)
    while x/5 < 4:
        x += 1
    # set minimum low y value
    y_value = math.ceil(x/4)
    while y_value % 5 != 0:
        y_value += 1
    incrementer = y_value
    y_values = []
    # fill in list of y values
    while len(y_values) < 4:
        y_values.append(y_value)
        y_value += incrementer
    return y_values


def set_all_y_values(numlist):
    """ Given a set of displayed y values, fills in the invisible y values.

    >>> set_all_y_values([5, 10, 15, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    >>> set_all_y_values([20, 40, 60, 100])
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 100]
    """
    increment = int(numlist[0] / 5)
    y_value = increment
    y_values = []
    while y_value <= numlist[-1]:
        y_values.append(y_value)
        y_value += increment
    return y_values


def print_histogram(printed_y_values, all_y_values, lengths_dict):
    # Populate missing x values for histogram purposes
    longest = max(lengths_dict.keys())
    for i in range(1, longest+1):
        if lengths_dict.get(i, None) is None:
            lengths_dict[i] = 0
    maxdigits = len(str(max(all_y_values)))
    # fill in a string for each line, from top to bottom
    histogram_lines = []
    for t in reversed(all_y_values):
        rowstr = ''
        if t in printed_y_values:
            rowstr = rowstr + str(t).rjust(maxdigits) + " -|"
        else:
            rowstr = rowstr + (" " * maxdigits) + "  |"
        for wlength in sorted(lengths_dict.keys()):
            if t > lengths_dict[wlength]:
                rowstr = rowstr + "   "
            else:
                rowstr = rowstr + "***"
        histogram_lines.append(rowstr)
    # fill in bottom of histogram
    rowstr = "0".rjust(maxdigits) + " -+" + ("-+-" * len(lengths_dict))
    histogram_lines.append(rowstr)
    lengths_list = sorted(lengths_dict.keys())
    rowstr = (' ' * maxdigits) + "  |" + str(lengths_list[0]).rjust(2)
    for wlength in lengths_list[1:]:
        rowstr = rowstr + str(wlength).rjust(3)
    histogram_lines.append(rowstr)
    for line in histogram_lines:
        print(line)


if __name__ == "__main__":
    # import doctest, final
    # doctest.testmod(final)

    # create dictionary of word lengths and their counts
    import sys
    try:
        filename = sys.argv[1]
        lengths_dict = create_word_length_dict(filename)
    except IOError:
        print("Unable to process your request. Please verify that the filename provided is correct.")
        sys.exit()
    except IndexError:
        print("Please provide a filename when running this program: './final.py filename.text'")
        sys.exit()

    # print dictionary of word lengths
    print("Length Count")
    for wlength, wcount in lengths_dict.items():
        print(wlength, wcount)

    print('')

    # print histogram of word lengths
    highest_count = max(lengths_dict.values())
    printed_y_values = set_printed_y_values(highest_count)
    all_y_values = set_all_y_values(printed_y_values)
    print_histogram(printed_y_values, all_y_values, lengths_dict)

