# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *
prime = [True for i in range(10**5+1)]

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

def SieveOfEratosthenes(n):

    
    p = 2
    while (p * p <= n):

        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    


def solve():
    
    n,m = linput()
    od = {}
    ans = [[0]*m for x in range(n)]
    if not prime[m]:
        for x in range(n):
            for y in range(m):
                ans[x][y] = x*m+y
    elif not prime[n]:
        for y in range(m):
            for x in range(n):
                ans[x][y] = y*n+x
    
    else:
        cols = [[0]*m for x in range(n)]



SieveOfEratosthenes(10**4)
for _ in range(int(input())):
    solve()