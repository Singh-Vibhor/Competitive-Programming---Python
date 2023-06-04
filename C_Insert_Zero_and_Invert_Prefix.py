# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n = int(input())
    l = linput()
    if l[n-1]!=0:
        print("NO")
        return
    
    ans = [0]
    i = 0
    for x in range(n-2,-1,-1):
        if l[x]==1 and x==0:
            ans.append(i+1)
            continue

        if l[x]==1 and l[x-1]==1:
            i+=1
            ans.append(0)
            continue

        if l[x]==1 and l[x-1]==0:
            ans.append(i+1)
            i=0

        if l[x]==0:
            ans.append(0)

    print("YES")
    printl(ans)

        


for _ in range(int(input())):
    solve()