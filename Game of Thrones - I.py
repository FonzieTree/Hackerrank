#!/bin/python3

import sys

def gameOfThrones(s):
    uchar=set(s)
    scount=[]
    for i in uchar:
        scount.append(s.count(i) % 2)
    if sum(scount)==1:
        return("YES")
    elif sum(scount)==0:
        return("YES")
    else:
        return("NO")
    # Complete this function

s = input().strip()
result = gameOfThrones(s)
print(result)
