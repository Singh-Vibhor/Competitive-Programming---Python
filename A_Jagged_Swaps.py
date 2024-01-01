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
    l = linput()
    ch = 1
    while ch:
        ch = 0
        for x in range(1,n-1):
            if l[x]>l[x-1] and l[x]>l[x+1]:
                temp = l[x]
                l[x] = l[x+1]
                l[x+1] = temp
                ch = 1
                break
    if l==sorted(l):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()