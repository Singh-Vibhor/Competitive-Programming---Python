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
    x,y,n = linput()
    ans = [x]
    
    ax = (y-x) - ((n-1)*(n-2))//2  
    if ax<n-1:
        print(-1)
        return
    
    ans.append(ans[-1]+ax)
    diff = n-2
    for z in range(2,n):
        ans.append(ans[-1]+diff)
        diff-=1
    printl(ans)



for _ in range(int(input())):
    solve()