#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    if (min(keyboards)+min(drives))>s:
        output=-1
    else:
        happy=[]
        for i in keyboards:
            for j in drives:
                if i+j<=s:
                    happy.append(i+j)
        output=max(happy)
    return(output)
    # Complete this function

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
