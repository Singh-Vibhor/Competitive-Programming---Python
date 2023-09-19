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
    s = input()
    n = len(s)
    m = int(input())
    a = input()
    b = input()

    c = -1

    for x in range(m):
        mp = dict()
        l = [y for y in range(int(a[x]),int(b[x])+1)]
        while True:
            c+=1
            if c == n:
                # print(x)
                print("YES")
                return
            mp[s[c]] = 1
            # print(mp,c,x)
            # print(l)
            f = 1
            for y in l:
                if str(y) not in mp:
                    f = 0
                    break
            if f:
                break
    print("NO")


for _ in range(int(input())):
    solve()