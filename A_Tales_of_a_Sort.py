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
    ans = 0
    for x in range(1,n):
        if l[x-1]>l[x]:
            ans = max(ans,l[x-1])
    print(ans)



for _ in range(int(input())):
    solve()