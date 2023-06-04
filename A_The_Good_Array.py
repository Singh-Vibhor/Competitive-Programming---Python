# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n,k = linput()
    ans = (n+k-1)//k
    if (n-1)%k and k!=1:
        ans+=1
    print(ans)



for _ in range(int(input())):
    solve()


