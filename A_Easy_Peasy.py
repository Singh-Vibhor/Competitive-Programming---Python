# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

pr = []

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
  
        if (prime[p] == True):
  
            
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            pr.append(p)

#SieveOfEratosthenes(10**5+1)

def solve():
    n=int(input())
    l=linput()
    gd = l[0]
    for x in l:
        gd = gcd(gd,x)
    if gd==1:
        print(0)
    else:
        for x in range(2,10000):
            if gcd(x,gd)==1:
                print(x)
                break
    
    



for _ in range(int(input())):
    solve()