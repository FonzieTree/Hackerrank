#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp)<=0 for a_temp in input().strip().split(' ')]
    if sum(a)<k:
        print('YES')
    else:
        print('NO')
