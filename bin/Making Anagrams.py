#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    total=len(s1)+len(s2)
    same=set(s1)&set(s2)
    baoliu=0
    for i in same:
        baoliu=baoliu+2*min(s1.count(i),s2.count(i))
    output=total-baoliu
    return(output)
    # Complete this function

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
