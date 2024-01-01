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

div = [x for x in range(10**5+1)]
def seive(n):
    for x in range(2,n):
        if div[x]==x:
            crr = x*x
            while crr<n:
                if div[crr]==crr:
                    div[crr] = x
                crr+=x
seive(10**5+1)

def solve():
    n = int(input())
    l = linput()
    l.sort()
    mp = {}


for _ in range(1):
    solve()