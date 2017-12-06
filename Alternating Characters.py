#!/bin/python3

import sys

def alternatingCharacters(s):
    count=0
    s=list(s)
    if len(s)>=2:
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count=count+1
    return(count)
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
