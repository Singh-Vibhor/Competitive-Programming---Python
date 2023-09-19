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

prime = [1]*(2*(10**5)+1)
for x in range(2,(2*(10**5)+1)):
    if prime[x]==1:
        prime[x] = x
        for y in range(x*x,(2*(10**5)+1),x):
            prime[y] = x



def solve():
    n = int(input())
    l = linput()
    c = Counter(l)
    ans = 0
    for x in range(1,n+1):
        mp = {}
        crr = 0
        while x>1:
            if prime[x] not in mp:
                crr+=c.get(prime[x],0)
            mp[prime[x]] = 1
            x//=prime[x]
        crr+=c.get(1,0)
        ans = max(ans,crr)
    print(ans)





for _ in range(int(input())):
    solve()