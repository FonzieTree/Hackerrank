#!/bin/python3

import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(len(arr))
while max(arr)!=min(arr):
    tmp=[]
    for i in arr:
        if i-min(arr)!=0:
            tmp.append(i-min(arr))
    arr=tmp
    print(len(arr))
    
