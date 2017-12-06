#!/bin/python3

import sys

def anagaram(s):
    if len(s) % 2 ==1:
        return(-1)
    else:
        s1=s[0:int(len(s)/2)]
        s2=s[int(len(s)/2):len(s)]
        total=len(s1)+len(s2)
        same=set(s1)&set(s2)
        baoliu=0
        for i in same:
            baoliu=baoliu+2*min(s1.count(i),s2.count(i))
        output=int((total-baoliu)/2)
        return(output)
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagaram(s)
    print(result)
