# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n = int(input())
    l = linput()
    a = max(l)
    a1 = []
    a2 = []
    for x in l:
        if a==x:
            a1.append(x)
        else:
            a2.append(x)
    if len(a1)==n:
        print(-1)
    else:
        print(len(a2),len(a1))
        printl(a2)
        printl(a1)




for _ in range(int(input())):
    solve()