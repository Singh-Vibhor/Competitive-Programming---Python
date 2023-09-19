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
    n=int(input())
    s = input()
    a = linput()
    
    cycles = []
    vs = [0]*(n+1)
    for x in range(1,n+1):
        if not vs[x]:
            cr = s[x-1]
            crr = a[x-1]
            while crr!=x:
                vs[crr] = 1
                cr+=s[crr-1]
                crr = a[crr-1]
            cycles.append(cr)
    ans = 1
    
    for x in cycles:
        y = x+x
        c = y[1:].find(x)+1
        # print(y,c)
        ans = lcm(ans,c)
    print(ans)
    




for _ in range(int(input())):
    solve()