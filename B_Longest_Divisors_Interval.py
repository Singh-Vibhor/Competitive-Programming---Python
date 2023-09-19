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
    for x in range(0,n):
        if n%(x+1)==0:
            ans+=1
        else:
            break
    print(ans)



for _ in range(int(input())):
    solve()