#!/usr/bin/env python
from sys import stdin

prev_word = None
words_cnt = 0

for line in stdin:
    word, one = line.strip().split(' ')
    one = int(one)

    if prev_word:
        if prev_word == word:
            words_cnt += one
        else:
            print(prev_word, words_cnt)
            words_cnt = one
            prev_word = word

    prev_word = word

print(prev_word, words_cnt)
