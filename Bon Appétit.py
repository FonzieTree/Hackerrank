#!/bin/python3
import sys
def bonAppetit(n, k, b, ar):
    ar.pop(k)
    ms=int(b-sum(ar)/2)
    if ms==0:
        ms="Bon Appetit"
    return(ms)
    # Complete this function
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
