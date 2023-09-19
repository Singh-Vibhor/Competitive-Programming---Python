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
    mp = {}
    for x in range(n):
        mp[l[x]-1] = x
    ans = 0
    for x in range(1,n):
        if mp[x-1]>mp[x]:
            ans+=1
    print(ans)



for _ in range(int(input())):
    solve()