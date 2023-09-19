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
    l = [linput() for _ in range(n)]
    l.sort(key = lambda x:x[1])
    #print(l)

    a, b = -1, -1
    ans = 0
    for x in l:
        if x[0]<=b:
            continue

        if a!=-1 and x[0]<=a:
            b = x[1]
            ans+=1
            a = -1
        
        else:
            a = x[1]
        
    print(n-(2*ans))



for _ in range(int(input())):
    solve()
