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

a = [0]*(10**6+1)
for y in range(2,1000):
    crr = (y**3)
    cur = (crr-1)//(y-1)
    while cur<(10**6+1):
        a[cur] = 1
        crr*=y
        cur = (crr-1)//(y-1)

def solve():
    n = int(input())
    if a[n]:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve()