#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function, find_anagrams(), which can be used to do the same
for an arbitrary list of strings.
"""

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = 'Veronica Fuentes and Kevin Clark'

import sys
from collections import defaultdict


def alphabetize(string):
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    anagrams = defaultdict(list)
    for w in words:
        anagrams[alphabetize(w)].append(w)
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        return(f"{k} : {v}")


if __name__ == "__main__":
    main(sys.argv[1:])
