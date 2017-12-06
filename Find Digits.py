#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    cf=list(str(n))
    count=0
    for i in cf:
        if int(i)!=0 and n % int(i) == 0:
            count=count+1
    print(count)
