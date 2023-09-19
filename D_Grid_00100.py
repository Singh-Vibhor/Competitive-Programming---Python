# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(''.join(map(str,l)))



def solve():
    n,k = linput()
    ans = [[0]*n for _ in range(n)]
    if k==0:
        print(0)
        for x in ans:
            printl(x)
        return
    cnt = k//n
    if k%n!=0:
        ansf=2
        g = k%n
        cnt+=1
    else:
        ansf=0
        g=-1
    
    for i in range(n):
        for j in range(cnt):
            ans[i][(i+j)%(n)] = 1
        if g>0:
            g-=1
        if g==0:
            cnt-=1
            g-=1
    
    print(ansf)
    for x in ans:
        printl(x)
    



for _ in range(int(input())):
    solve()