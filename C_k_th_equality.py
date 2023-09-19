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

def prfsm(n):
    return (n*(n+1))//2

def totalpos(a):
    return prfsm(a)-prfsm(a-1)

def solve():
    a,b,c,k = linput()
    if c>a+b or c<max(a,b):
        print(-1)
    
    else:
        pass
    




for _ in range(int(input())):
    solve()