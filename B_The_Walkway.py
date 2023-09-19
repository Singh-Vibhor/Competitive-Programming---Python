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
    n,m,d = linput()
    l = linput()
    if l[0]!=1:
        l1 = [1]+l
    else:
        l1 = l
    # if l[-1]!=n:
    #     l.append(n)
    # if l[0]!=1:
    #     l = [1]+l
    prv = 0
    cnt = 0
    if l[0]!=1:
        cnt = 1
        prv = 1

    for x in l:
        cnt += (x-prv-1)//d
        cnt+=1
        prv = x
    cnt+=(n-prv)//d
    ans = 0
    
    # print(cnt)
    for y in range(1,len(l1)-1):
        if l1[y]%d>l1[y-1]%d:
            if l1[y+1]%d>l1[y]%d or l1[y+1]%d<=l1[y-1]%d:
                ans+=1
                
        elif l1[y]%d<l1[y-1]%d:
            # print("hi")
            # print(l1[y]%d, l1[y-1]%d, l1[y+1]%d)

            if l1[y+1]%d<=l1[y-1]%d and l1[y+1]%d>l1[y]%d   :
                ans+=1
        elif l1[y+1]-l1[y-1]<=d:
            ans+=1
    
    # prv curr next
    # (next-prv-1)/d+1
    # (curr-prv-1)/d+1 + (next-curr-1)/d+1
                
    
    if (n-l1[-2])//d < ((l1[-1]-l1[-2]-1)//d +1+(n-l1[-1])//d):
        ans+=1

    # print(ans)
    if ans>=1:
        print(cnt-1,ans)
    else:
        print(cnt,m)

# 9
# 7 11 21
# 7 6 5 4 3
# 2 7 21
# 8 0 1 2
for _ in range(int(input())):
    solve()