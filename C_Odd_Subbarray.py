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
    n=int(input())
    l=linput()
    l1 = []
    for x in range(n):
        if ceil(sqrt(l[x]))==floor(sqrt(l[x])):
            l1.append(x)
    ans = 0
    eve, odd = 0, 0
    if len(l)>0:
        ans+=l[0]+1
        eve = l[0]
    if len(l)>1:
        ans+=(l[1]-l[0])
        odd = l[1]-l[0]

    for x in range(2,len(l1)):
        if x==len(l1)-1:
            ls = n
        else:
            ls = l1[x+1]
        
        if x%2:
            ans+= odd*(ls-l[x])
            odd+=ls-l[x]
        else:
            ans+= eve*(ls-l[x])
            eve+=(ls-l[x])
    
    print(ans)




for _ in range(int(input())):
    solve()