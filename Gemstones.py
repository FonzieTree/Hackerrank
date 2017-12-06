#!/bin/python3

import sys

def gemstones(arr):
    out=set(arr[0])
    for i in arr:
        out=out&set(i)
    return(out)
    # Complete this function

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
    
result = gemstones(arr)
print(len(result))
