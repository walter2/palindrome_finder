#!/user/bin/python3


import string


class WordFinder():
    '''class WordFinder() requires a function (that describes the word)
       and a minimum word length.
       It keeps track of words that were already found.
    '''
    def __init__(self, function, min_result_length):
        self.function = function
        self.min_result_length = min_result_length
        self.found_words = []

    def process_string(self, input_string):
        '''process_string() looks for the specified alphabetical words
           in the provided string. It updates self.found_words
           if it finds new words and retruns the newly found words.
           Punctuation is removed from the input_string.
        '''
        found_words_in_string = []
        for punctuation in string.punctuation:
            input_string = input_string.replace(punctuation, ' ')
        word_list = input_string.split(' ')
        for word in word_list:
            if len(word) >= self.min_result_length and word.isalpha():
                if self.function(word) \
                   and word.lower() not in self.found_words:
                    found_words_in_string.append(word)
                    self.found_words.append(word.lower())
        return found_words_in_string
