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
    n,m = linput()
    l1 = linput()
    l2 = linput()
    l3 = linput()
    mp = defaultdict(list)
    for x in range(n):
        if l1[x]!=l2[x]:
            mp[l2[x]].append(x)
    
    if l3[-1] not in l2:
        print("NO")
        return
    
    if len(mp[l3[-1]]):
        tmp = mp[l3[-1]].pop()
    else:
        tmp = l2.index(l3[-1])

    ans = [0]*m
    for x in range(m):
        if len(mp[l3[x]]):
            ans[x] = mp[l3[x]].pop()+1
        else:
            ans[x] = tmp+1
        l1[ans[x]-1] = l3[x]
    
    if l1!=l2:
        print("NO")
        return
    
    print("YES")
    printl(ans)

    




for _ in range(int(input())):
    solve()