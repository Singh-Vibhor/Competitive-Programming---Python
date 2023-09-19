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
    ans = 0
    n = int(input())
    for x in range(n):
        a,b = linput()
        if a>b:
            ans+=1
    print(ans)



for _ in range(int(input())):
    solve()