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
    n = int(input())
    l=linput()
    a = l.index(1)
    if len(l)==1:
        print(1,1)
        return
    b = l.index(2)
    c = l.index(max(l))
    if abs(a-b)>1:
        if a<b:
            print(a+2,c+1)
        else:
            print(a,c+1)
    else:
        if (b>a and c<a) or (b<a and c>a):
            print(a+1,c+1)
        else:
            print(b+1,c+1) 







for _ in range(int(input())):
    solve()