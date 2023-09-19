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
    n,m,q = linput()
    s = input()
    tree = [0] * (2 * n)
    f = [0]*(n)

    def update(l, r, x):
        l+=n
        r+=n
        while l<r:
            if l&1:
                if tree[l]!=0:
                    tree[l] = min(tree[l],x)
                else:
                    tree[l] = x 
                l+=1
            
            if r&1:
                r-=1
                if tree[r]!=0:
                    tree[r] = min(tree[r],x)
                else:
                    tree[r] = x 
                
            
            l>>=1
            r>>=1

    def query(q):
        q+=n
        while q>=1:
            if tree[q]:
                return tree[q]
            q>>=1
        return 0

    for x in range(m):
        seg = linput()
        update(seg[0]-1, seg[1], x+1)
    
    mp = defaultdict(str)
    for x in range(n):
        mp[str(query(x-1))]+=s[x]
    a1 = ""
    for x in sorted(list(mp.keys())):
        a1+=mp[x]


    for x in range(q):
        qr = int(input())
        print(a1)
        # print(query(qr-1))
    




for _ in range(1):
    solve()