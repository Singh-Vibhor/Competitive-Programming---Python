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
    n,k = linput()
    l = linput()
    ans = 0
    for i,x in enumerate(l):
        ans+=x//k
        l[i] = x%k

    l.sort()
    p1 = 0
    p2 = n-1
    
    while p1<p2:
        if l[p1]+l[p2]>=k:
            ans+=1
            p1+=1
            p2-=1
        else:
            p1+=1
    print(ans)



for _ in range(int(input())):
    solve()