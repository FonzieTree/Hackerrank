#!/bin/python3

import sys

ss=['h','a','c','k','e','r','r','a','n','k']
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    s=list(s)
    hid=[x for x in range(len(s)) if s[x]=='h']
    if hid!=[]:
        s=s[hid[0]+1:]
        aid=[x for x in range(len(s)) if s[x]=='a']
        if aid!=[]:
            s=s[aid[0]+1:]
            cid=[x for x in range(len(s)) if s[x]=='c']
            if cid!=[]:
                s=s[cid[0]+1:]
                kid=[x for x in range(len(s)) if s[x]=='k']
                if kid!=[]:
                    s=s[kid[0]+1:]
                    eid=[x for x in range(len(s)) if s[x]=='e']
                    if eid!=[]:
                        s=s[eid[0]+1:]
                        rid=[x for x in range(len(s)) if s[x]=='r']
                        if rid!=[]:
                            s=s[rid[0]+1:]
                            rid=[x for x in range(len(s)) if s[x]=='r']
                            if rid!=[]:
                                s=s[rid[0]+1:]
                                aid=[x for x in range(len(s)) if s[x]=='a']
                                if aid!=[]:
                                    s=s[aid[0]+1:]
                                    nid=[x for x in range(len(s)) if s[x]=='n']
                                    if nid!=[]:
                                        s=s[nid[0]+1:]
                                        kid=[x for x in range(len(s)) if s[x]=='k']
                                        if kid!=[]:
                                            print('YES')
                                        else:
                                            print('NO')
                                    else:
                                        print('NO')
                                else:
                                    print('NO')
                            else:
                                print('NO')
                        else:
                            print('NO')
                    else:
                        print('NO')
                else:
                    print('NO')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
# your code goes here
