#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
area=[]
for char in word:
    area.append(h[ord(char)-ord('a')])
print(max(area)*len(word))
