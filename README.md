Palindrome finder
==========

The palindrome finder is a Python3 program that detects palindromes in a string.
The program is designed to run from the command line.

find_palindrome.py runs from the command line. Input is given there and the result are displayed there as well. 
Each found palindrome is only listed once. The program keeps track of already found palindromes. 

The program terminates by pressing enter.


Usage:
------
$python3 find_palindrome.py
Bob wants a racecar.

Bob
racecar

Anna does disagree and Bob is not happy. They decide to eat ice cream at noon to settle the matter.

Anna
noon


$


Contents:
--------
find_palindrome.py is the main program.

is_palindrome.py defines what a palindrome is and tests given input if it is a palindrome. It returns True or False. One character words are considered as 
palindromes as well. Palindromes can be alpha-numeric.

word_finder.py contains the class WordFinder which finds any words that are defined through a function. At instantiation the word defining function needs to be provided with the maximum word length.
Only purely alphabetic words are considered as words. WordFinder.process_string() searches for defined words in a given string.

test_is_palindrome.py and test_WordFinder.py contain the test suit for the function and class.

Written in Python 3.3.
