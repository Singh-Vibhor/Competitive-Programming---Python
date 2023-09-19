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

mp = {}
for y in range(2,1000001):
    crr = (y**3)
    cur = (crr-1)//(y-1)
    while cur<=(10**18+1):
        mp[cur] = 1
        crr*=y
        cur = (crr-1)//(y-1)



def solve():
    n = int(input())
    if n in mp:
        print("YES")
    else:
        # st = 2
        # en = 10**9+1
        # while st<en-1:
        #     mid = (st+en)//2
        #     crr = mid**3
        #     cur = (crr-1)//(mid-1)
        #     if cur==n:
        #         print("YES")
        #         return
        #     if crr<n:
        #         st = mid
        #     else:
        #         en = mid
        # crr = 1000007**3
        # cur = (crr-1)//(1000007-1)
        # if cur==n:
        #     print("YES")
        #     return
        
        a = int(sqrt(n))
        if a>1:
            crr = a**3
            cur = (crr-1)//(a-1)
            if cur==n:
                print("YES")
                return
        print("NO")



for _ in range(int(input())):
    solve()