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
    l = linput()
    l1 = l.copy()
    opr = 0
    ans = []
    for x in range(1,n):
        while l1[x]<l1[x-1]:
            a = max(l1)
            ind = l1.index(a)
            opr+=1
            l1[x]+=a
            ans.append([x+1,ind+1])
            if opr>50:
                break
    if opr<=50:
        print(opr)
        if len(ans):
            print("\n".join([str(x[0])+" "+str(x[1]) for x in ans]))
        return
    
    opr = 0
    l1 = l.copy()
    ans = []
    for x in range(n-2,-1,-1):
        while l1[x+1]<l1[x]:
            a = min(l1)
            ind = l1.index(a)
            opr+=1
            l1[x]+=a
            ans.append([x+1,ind+1])
            if opr>50:
                break
    if opr<=50:
        print(opr)
        if len(ans):
            print("\n".join([str(x[0])+" "+str(x[1]) for x in ans]))
        return
            



for _ in range(int(input())):
    solve()