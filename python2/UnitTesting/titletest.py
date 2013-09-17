""" Puts strings into title case """
import unittest

def title(s):
    wordlist = s.split()
    results = []
    for w in wordlist:
        results.append(w[0].upper()+w[1:])
    return " ".join(results)

class TestTitle(unittest.TestCase):

    def test_short_string(self):
        base_str = "hi there"
        teststr1 = title(base_str)
        teststr2 = base_str.title()
        self.assertEqual(teststr1, teststr2, \
            "Results of two title-case functions do not match for string 'hi there'")

    def test_longer_string(self):
        base_str = "this is a slightly longer string for more testing"
        teststr1 = title(base_str)
        teststr2 = base_str.title()
        self.assertEqual(teststr1, teststr2, \
            "Results of two title-case functions do not match for string 'this is a slightly longer string for more testing'")

if __name__ == "__main__":
    unittest.main()

