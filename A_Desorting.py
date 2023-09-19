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
    ans = 10**9
    for x in range(1,n):
        ans = min(ans,max((l[x]-l[x-1]+2)//2,0))
    print(ans)



for _ in range(int(input())):
    solve()