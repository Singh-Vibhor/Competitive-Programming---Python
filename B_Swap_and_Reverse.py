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
    n,k = linput()
    # s1 = "abcdefghijklmnopqrstuvwxyz"
    s = input()
    s = s[:n]
    # print(s)
    if k%2==0:
        print("".join(sorted(s)))
    else:
        s1 = []
        s2 = []
        f = 0
        for x in s:
            if f:
                s1.append(x)
            else:
                s2.append(x)
            f = 1-f
        s1.sort()
        s2.sort()
        # print(s1,s2)
        ans = []
        for x in range(len(s1)):
            ans.append(s2[x])
            ans.append(s1[x])
        if len(s1)!=len(s2):
            ans.append(s2[-1])
        print("".join(ans))
            



for _ in range(int(input())):
    solve()