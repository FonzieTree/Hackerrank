#!/bin/python3

import sys

def solve(n, p):
    groupp=round((p/2)+0.9)
    groupn=round((n/2)+0.9)
    out=min(groupn-groupp,groupp-1)
    # Complete this function
    return(out)
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
