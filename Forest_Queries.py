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
    n,q = linput()
    l = []
    for x in range(n):
        s = input()
        l.append(s)

    a1 = [[0]*n for x in range(n)]
    for i in range(n):
        for j in range(n):
            if l[i][j] == '*':
                a1[i][j] = 1
            if i!=0:
                a1[i][j] += a1[i-1][j]
            if j!=0:
                a1[i][j] += a1[i][j-1]
            if i!=0 and j!=0:
                a1[i][j] -= a1[i-1][j-1]
    
    for x in range(q):
        x1, y1, x2, y2 = linput()
        ans = a1[x2-1][y2-1]
        if x1!=1:
            ans -= a1[x1-2][y2-1]
        if y1!=1:
            ans -= a1[x2-1][y1-2]
        if x1!=1 and y1!=1:
            ans += a1[x1-2][y1-2]
        print(ans)
    
        


for _ in range(1):
    solve()