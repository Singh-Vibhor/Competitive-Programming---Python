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
    n,m = linput()
    cnt = 0
    ans = 0
    while cnt<50:
        n = n%m
        if n==0:
            print(ans)
            return
        ans+=n
        n*=2
        cnt+=1
    print(-1)





for _ in range(int(input())):
    solve()