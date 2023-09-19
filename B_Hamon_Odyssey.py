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
    cr = l[0]
    ans = 0
    for x in l[1:]:
        if cr==0:
            cr = x
            ans+=1
        else:
            cr&=x
    if cr==0:
        ans+=1
    if ans==0:
        print(1)
        return
    print(ans)



for _ in range(int(input())):
    solve()