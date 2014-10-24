#!/user/bin/python3

'''
Tests for WordFinder class.
'''

import string
import sys
import unittest

from is_palindrome import is_palindrome
from word_finder import WordFinder

MIN_PALINDROME_LENGTH = 2


class TestWordFinder(unittest.TestCase):

    def setUp(self):
        self.palindrome_finder = WordFinder(is_palindrome, MIN_PALINDROME_LENGTH)

    def test_WordFinder_minimum_word_length_is_set_to_two_characters(self):
        expected = ['Anna']
        actual = self.palindrome_finder.process_string('Anna is a girl.')
        self.assertEqual(expected, actual)

    def test_WordFinder_minimum_word_length_is_set_to_three_characters(self):
        palindrome_finder = WordFinder(is_palindrome, 3)
        expected = ['Bob', 'Anna']
        actual = palindrome_finder.process_string('Bob and Anna!')
        self.assertEqual(expected, actual)

    def test_WordFinder_minimum_word_length_is_set_to_four_characters(self):
        palindrome_finder = WordFinder(is_palindrome, 4)
        expected = ['Anna']
        actual = palindrome_finder.process_string('Bob and Anna!')
        self.assertEqual(expected, actual)

    def test_repeated_words_are_only_captured_once(self):
        expected = ['Anna']
        actual = self.palindrome_finder.process_string(
            'Anna has a sister but her name is not Anna!.'
            )
        self.assertEqual(expected, actual)

    def test_different_case_words_are_detected_as_the_same_word(self):
        expected = ['Anna']
        actual = self.palindrome_finder.process_string(
            'Anna is normally spelled with a capital character but sometinmes as anna.'
            )
        self.assertEqual(expected, actual)

    def test_WordFinder_only_returns_alphabetic_words(self):
        expected = ['Bob', 'Anna']
        actual = self.palindrome_finder.process_string(
            'Bob does not have a t3sts3t but a rac&e&car like Anna!'
            )
        self.assertEqual(expected, actual)
        
    def test_WordFinder_removes_punctuation_correctly(self):
        expected = ['Bob', 'Anna']
        actual = self.palindrome_finder.process_string('Bob and Anna!')
        self.assertEqual(expected, actual)

    def test_WordFinder_keeps_track_of_already_detected_words(self):
        expected = ['Bob']
        self.palindrome_finder.process_string('Anna has a sister.')
        actual = self.palindrome_finder.process_string(
            'Anna has a brother which is called Bob.'
            )
        self.assertEqual(expected, actual)
        

if __name__ == "__main__":
    unittest.main(exit = False)
