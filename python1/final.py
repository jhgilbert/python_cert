#!/usr/local/bin/python3
""" Prints a table showing a word count for each of the word lengths encountered. """

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
    del lengths[0]

    return lengths

def _test():
    import doctest, final
    return doctest.testmod(final)

if __name__ == "__main__":
    import sys
    try:
        filename = sys.argv[1]
        lengths_dict = create_word_length_dict(filename)
        print("Length Count")
        for length, count in lengths_dict.items():
            print("{0} {1}".format(length, count))
    except IOError:
        print("Unable to process your request. Please verify that the filename provided is correct.")
    except IndexError:
        print("Please provide a filename when running this program: './final.py filename.text'")
