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
    fxp, fxn, fyp, fyn = 0, 0, 0, 0
    for x in range(n):
        a,b = linput()
        if a>0:
            fxp = 1
        elif a<0:
            fxn = 1
        
        if b>0:
            fyp = 1
        elif b<0:
            fyn = 1

    if fxp and fxn and fyp and fyn:
        print("NO")
    else:
        print("YES")



for _ in range(int(input())):
    solve()