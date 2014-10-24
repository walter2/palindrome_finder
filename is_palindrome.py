#!/user/bin/python3


def is_palindrome(value):
    '''is_palindrome() returns True if the given string is
       a palindrome or Flase otherwise.
       Raises ValueError if the input is a not a string or an empty string.
       Note that one letter or alpha-numeric words are considered
       polindroms as well.
    '''
    if not isinstance(value, str) or len(value) < 1:
        raise ValueError    
    value = value.lower()
    is_value_palindrome = False
    if value == value[::-1]:
        is_value_palindrome = True
    
    return is_value_palindrome
