#!/user/bin/python3

'''
find_palindromes.py is run from the command line.
It takes text input from stdin and finds all the palindromes
in the given text.
The found palindromes are printed in order to the console.
'''

import sys

from is_palindrome import is_palindrome
from word_finder import WordFinder


MIN_PALINDROME_LENGTH = 2


def process_stdin():
    '''process_stdin() takes the stdin line by line and 
       uses the class WordFinder with the is_palindrome() function
       to find all the palindromes with a given length in it.
       The found palindromes are printed right back to the console.
       The function terminates by pressing Enter.
    '''
    palindrome_finder = WordFinder(is_palindrome, MIN_PALINDROME_LENGTH)
    try:
        for line in sys.stdin:
            if line.rstrip() == '':
                break
            palindromes_in_line = palindrome_finder.process_string(line.rstrip())
            print('')
            for palindrome in palindromes_in_line:
                print(palindrome)
            print('')
    except Exception as msg:
        print(msg)   

           
if __name__ == '__main__':
    process_stdin()
