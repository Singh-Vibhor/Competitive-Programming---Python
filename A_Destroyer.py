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
    c = Counter(l)
    for x in range(1,max(l)+1):
        #print(c.get(x,0),c.get(x-1,0))
        if c.get(x,0)>c.get(x-1,0):
            print("NO")
            return
    print("YES")



for _ in range(int(input())):
    solve()