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
    l = linput()
    
    mp = defaultdict(list)
    for i,x in enumerate(l):
        mp[x].append(i)
    
    ans = n
    for y in mp.keys():
        l = mp[y]
        longest,secondlongest = max(l[0], n - l[len(l)-1] - 1), min(l[0], n - l[len(l)-1] - 1)
        # print(longest,secondlongest,y)
        for x in range(1,len(l)):
            if l[x]-l[x-1]-1>=longest:
                secondlongest = longest
                longest = l[x]-l[x-1]-1
            
            elif l[x]-l[x-1]-1>secondlongest:
                secondlongest = l[x]-l[x-1]-1
        if longest==1 and secondlongest==0:
            ans = 0
        ans = min(ans,max(secondlongest,(longest)//2))
    print(ans)
        



for _ in range(int(input())):
    solve()