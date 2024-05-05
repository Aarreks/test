# Alex Giang
# Professor Abolghasemi
# CIS 502
# 29 February 2024

# Week 6, Exercise 2

# This file is intended to demonstrate beginning knowledge in implementing
# iterator classes with customized behavior.

import collections.abc


class CapitalizeIterator(collections.abc.Iterator):
    def __init__(self, words):
        if isinstance(words, list):
            pass
        elif isinstance(words, str):
            words = words.split()
        else:
            raise TypeError(words, 'Please pass CapitalizeIterator constructor either a'
                                   ' list of words or a string')
        self.words = []
        for w in words:
            if len(w) >= 1:
                self.words.append(w[:1].upper() + w[1:].lower())

    def __next__(self):
        if self.words:
            return self.words.pop(0)
        else:
            raise StopIteration


word_list_list = [
    ["python", "is", "awesome"],
    "returning each word capitalized",
    ["java", "wouldn't", "allow", "this"],
    "ha ha ha hee ha ha"
]
for wl in word_list_list:
    iterator = iter(CapitalizeIterator(wl))
    print('\nCapitalized words:')
    for wd in iterator:
        print(wd, end=' ')
