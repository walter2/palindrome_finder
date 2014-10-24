#!/user/bin/python3

'''
Tests for the is_palindrome function.
'''

import unittest

from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase): 
    def test_A_is_a_palindrome(self):
        actual = is_palindrome('A')
        self.assertTrue(actual)

    def test_ann_is_not_a_palindrome(self):
        actual = is_palindrome('ann')
        self.assertFalse(actual)
    
    def test_even_length_word_is_a_palindrome(self):
        actual = is_palindrome('anna')
        self.assertTrue(actual)

    def test_odd_length_word_is_a_palindrome(self):
        actual = is_palindrome('detartrated')
        self.assertTrue(actual)

    def test_upper_case_word_is_a_palindrome(self):
        actual = is_palindrome('Anna')
        self.assertTrue(actual)

    def test_UTF_8_characters_are_in_palindrome(self):
        actual = is_palindrome('Анна')
        self.assertTrue(actual)

    def test_is_palindrome_raises_exception_for_empty_string(self):
        with self.assertRaises(ValueError):
            is_palindrome('')
    
    def test_is_palindrome_raises_exception_for_None_input(self):
        with self.assertRaises(ValueError):
            is_palindrome(None)
    
    def test_is_palindrome_raises_exception_for_number_input(self):
        with self.assertRaises(ValueError):
            is_palindrome(888)

if __name__ == "__main__":
    unittest.main(exit = False)
