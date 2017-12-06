#!/bin/python3

import sys
import math
def sockMerchant(n, ar):
    myset=set(ar)
    out=sum([math.floor(ar.count(item)/2) for item in myset])
    # Complete this function
    return(out)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
