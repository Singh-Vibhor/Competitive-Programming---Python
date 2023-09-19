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



def solve():
    n = int(input())
    mp = {}
    f = 0
    for x in range(n):
        s = input()
        s = s[:len(s)-1]
        # a = input()
        # print(len(s),s)
        if f:
            continue
        if len(s)==1:
            f = 1
            continue

        if len(s)==2:
            mp[s] = ""
            a = s[::-1]
            if a in mp:
                f = 1
            continue

        mp[s] = True
        mp[s[:2]] = s[2]
        if s[::-1] in mp:
            f = 1
            continue
        a = s[1:]
        a = a[::-1]
        if a in mp:
            if mp[a]=="":
                f = 1
    if f:
        print("YES")
    else:
        print("NO")

        




for _ in range(int(input())):
    solve()