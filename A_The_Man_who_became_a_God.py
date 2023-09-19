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
    l1 = []
    for x in range(1,n):
        l1.append(abs(l[x]-l[x-1]))
    l1.sort(reverse = True)
    ans = sum(l1[k-1:])
    print(ans)



for _ in range(int(input())):
    solve()