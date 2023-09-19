# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n=int(input())
    l=linput()
    ans = ["1"]
    prv = l[0]
    f=0
    first = l[0]
    for x in range(1,n):
        if l[x]>prv:
            if f==0:
                ans.append("1")
                prv = l[x]
            else:
                if l[x]<=first:
                    ans.append("1")
                    prv = l[x]
                else:
                    ans.append("0")
        else:
            if l[x]==prv:
                ans.append("1")
            else:
                if f==0 and l[x]<=first:
                    f=1
                    ans.append("1")
                    prv = l[x]
                
                else:
                    ans.append("0")

    print("".join(ans))





for _ in range(int(input())):
    solve()