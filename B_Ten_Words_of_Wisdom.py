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
    ans = -1
    mx = -1
    n = int(input())
    for x in range(n):
        a,b = linput()
        if a<=10 and b>mx:
            ans = x+1
            mx = b
    print(ans)



for _ in range(int(input())):
    solve()