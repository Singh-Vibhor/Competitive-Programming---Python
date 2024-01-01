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
    n,k = linput()
    s = input()
    if s[-1] not in ['U', 'S', 'R']:
        s = s[:len(s)-1]
    mv = 1
    crr = 0
    for x in s:
        # print(crr, x)
        if x=='R':
            mv = -mv
        
        if x=='S':
            # print(crr)
            crr = (n+crr+(2*mv))%n
            # print(crr)
            # continue
        else:
            crr = (n+crr+mv)%n
        # print(crr, x)

    print(crr+1)




for _ in range(int(input())):
    solve()