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
    ans = 0
    for x in range(n):
        l = list(range(1,x+1))+ list(range(n,x,-1))
        ans1 = 0
        mx = 0
        for x in range(n):
            mx = max(l[x]*(x+1),mx)
            ans1 += l[x]*(x+1)
        ans = max(ans1-mx,ans)
    print(ans)



for _ in range(int(input())):
    solve()