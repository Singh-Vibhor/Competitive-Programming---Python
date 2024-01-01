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
    l = linput()
    mn = 100
    for ans in range(1,68):
        mp = {}
        crr = 2**ans
        for x in l:
            mp[x % crr] = 1
        if len(mp.keys()) == 2:
            break
    print(2**ans)



for _ in range(int(input())):
    solve()