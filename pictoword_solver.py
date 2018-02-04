"""
Provides possible solutions to puzzles in the iOS app Pictoword.

Update word_dicts with names of word lists.  Recommended word lists included, along with sources.

Dictionaries not included due to lack of desire to figure out licensing restrictions.
"""

from collections import Counter
from datetime import datetime
import os

word_dicts = [
    '/usr/share/dict/words',  # Included with Linux distros
    '3esl.txt',  # 23k words from http://wordlist.aspell.net/12dicts/
    '6of12.txt',  # 34k words from http://wordlist.aspell.net/12dicts/
    '2of12.txt',  # 41k words from http://wordlist.aspell.net/12dicts/
    '2of12inf.txt',  # 82k words from http://wordlist.aspell.net/12dicts/
    'en_US.dic',  # 49k words from https://sourceforge.net/projects/hunspell/files/Spelling%20dictionaries/en_US/
    'words.txt',  # 467k words from https://github.com/dwyl/english-words
]


def pictoword_solver():
    """
    Queries letters that are available and the number of letters in the answer.  Prints the list of possible answers.
    Iterates over the dictionaries listed in word_dicts and compiles a list of possible answers from each.
    """
    letters = input('Enter letters: ')
    num_letters = int(input('How many letters in answer?: '))

    start = datetime.now()
    # print(f'Starting at {start}')

    possible_answers = set()

    for word_file in word_dicts:
        if os.path.isfile(word_file):
            possible_answers = possible_answers | set(elimate_by_set(letters, num_letters, word_file))
        else:
            print(f'{word_file} was not found. Skipping...')

    print(f'Took {(datetime.now() - start).total_seconds()} seconds')

    print('{} possible answers:\n{}'.format(len(possible_answers), "\n".join(sorted(possible_answers))))


def word_in_letters(word, letter_string):
    """
    Checks to ensure that all of the characters in word are in the letters string.
    """
    letter_count = Counter(letter_string)
    word_count = Counter(word)
    for letter in word_count:
        if letter_count[letter] < word_count[letter]:
            return False
    return True


def elimate_by_set(letters, num_letters, word_file):
    """
    Fastest way I've found to figure out which words of num_letters length are possible in the list of letters by
    checking for their existence in the word_file.

    Logic:
    Create dictionary from the word_file with the form:  { word: set(word), ...} using only words that have the same
    length as the solution (num_letters).  Note that set(word) is the list of unique letters in the word.
    Iterate through this dictionary and check to see if the unique letters in the word are also in the list of letters.
    If so, check to see if the string of letters have enough of each letter that is required by the word.
    If so, this is a possible solution to the problem!

    The primary source of the speed of this algorithm is due to using set to find unique letters in the word.  By doing
    this, and by limiting the words to only those with the required length, we severely limit the number of words to
    check and the time it takes to find a first order match (same unique letters).  After this, it's trivial to check
    that the list of letters have enough of each character for the word to be a possible answer.
    :param letters: List of letters that can be used to create the solution word
    :param num_letters: The number of letters in the solution word
    :param word_file: Text file that is a list of words.
    :return: List of words that may be an answer
    """
    possible_answers = []

    letters = letters.lower()

    letter_set = set(letters)

    with open(word_file) as wordfile:
        words = wordfile.read()

    word_dict_set = {word: set(word)
                     for word in words.replace("'", '').split()
                     if len(word) == num_letters}

    for word, word_set in word_dict_set.items():
        if word_set & letter_set == word_set:  # Does the letter set have the unique letters required by the word?
            if word_in_letters(word, letters):  # If so, does it contain all copies of the letters that are required?
                possible_answers.append(word)  # We have a (possible) winner!!

    return possible_answers


if __name__ == '__main__':
    pictoword_solver()
