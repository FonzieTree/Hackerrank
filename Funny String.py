#!/bin/python3

import sys

def funnyString(s):
    rd=[]
    ld=[]
    right=list(s)[0:(len(s))]
    left=list(s[::-1])[0:(len(s))]
    for i in range(1,len(s)):
        rd.append(abs(ord(right[i])-ord(right[i-1])))          
        ld.append(abs(ord(left[i])-ord(left[i-1])))
    if rd==ld:
        out="Funny"
    else:
        out="Not Funny"
    return(out)
    # Complete this function

q = int(input().strip())

for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
