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



#remember binary search
#bitwise operator -> bitmask
def solve():
    n = int(input())
    a = linput()
    b = linput()
    c = linput()
    f = [0]*n
    intervals = []
    a.sort()
    b.sort()
    p1 = 0
    p2 = 0
    while 1:
        if p1+1 >= n:
            break
        while p1+1 < n and a[p1+1]<b[p2]:
            p1+=1  
        f[p1] = 1
        intervals.append(b[p2] - a[p1])
        p1+=1
        p2+=1
    
    for x in range(n-1,-1,-1):
        if f[x] == 0:
            intervals.append(b[p2] - a[x])
            p2+=1
    
    print(intervals)
        



for _ in range(int(input())):
    solve()