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
    l1 = linput()
    l2 = linput()
    l3 = []
    for x in range(n):
        l3.append(l1[x]-l2[x])
    ans = []
    mx = max(l3)
    for x in range(n):
        if l3[x]==mx:
            ans.append(x+1)
    print(len(ans))
    printl(ans)



for _ in range(int(input())):
    solve()