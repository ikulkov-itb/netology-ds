#!/usr/bin/env python
from sys import stdin

for line in stdin:
    words = line.strip().split(',')[0]
    for word in words.split(' '):
        if word:
            print(word, 1)
