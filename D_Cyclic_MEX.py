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



#remember binary search
#bitwise operator -> bitmask
def solve():
    n = int(input())
    l = linput()
    r = l.index(0)

    l = l[r:] + l[:r]

    ans = [n]*n
        
    st = [(0,0)]
    for x in range(1,n):
        while l[x] < st[-1][0]:
            st.pop()
        
        ind  = st[-1][1]
        ans[x] = ans[ind] + (x-ind)*l[x]
        st.append((l[x],x))
    
    print(max(ans))
            


for _ in range(int(input())):
    solve()