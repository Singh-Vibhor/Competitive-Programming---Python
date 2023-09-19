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
    n,d,h = linput()
    l = linput()
    l.sort()
    ans = (h*d)/2*(n)
    for x in range(1,n):
        if l[x]-l[x-1]<h:
            d1 = d*(h-l[x]+l[x-1])/h
            # print(d1,x,l[x]-l[x-1])
            ans-= (d1*(h-l[x]+l[x-1]))/2
    print(ans)



for _ in range(int(input())):
    solve()