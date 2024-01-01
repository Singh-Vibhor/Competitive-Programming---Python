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

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]



def solve():
    n = int(input())
    t1 = defaultdict(list)
    t2 = defaultdict(list)

    for x in range(n-1):
        a,b = linput()
        t1[a].append(b)
        t1[b].append(a)
    
    for x in range(n-1):
        a,b = linput()
        t2[a].append(b)
        t2[b].append(a)




for _ in range(1):
    solve()