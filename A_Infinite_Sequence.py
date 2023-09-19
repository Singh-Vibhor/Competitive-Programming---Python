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
    n=int(input())
    if n==2:
        print(1)
        return
    if n==3:
        print(2)
        return
    for x in range(n):
        if (x*(x+1))//2>=n:
            break
    print(n - ((x*(x-1))//2))



for _ in range(1):
    solve()