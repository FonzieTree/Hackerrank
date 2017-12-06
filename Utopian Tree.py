#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())+1
    out=0
    for i in range(n):
        if i % 2 == 0:
            out=out+1
        else:
            out=out*2
    print(out)
