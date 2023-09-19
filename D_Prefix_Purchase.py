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
    c = linput()
    k = int(input())
    # c1 = sorted(c)
    # m1 = {}
    # for x in range(n):
    #     m1[str(c[x])] = x
    
    # p1 = 0
    # a1 = []
    # while k>0 and p1<n:
    #     # print(k,c1[p1])
    #     if k>c1[p1]:
    #         add = k//c1[p1]
    #         # print(add,x)
    #         a1.append((m1[str(c1[p1])],add))
    #         k -= add*(c1[p1])
    #     p1+=1
    
    # if len(a1):
    #     g = a1[-1]
    #     k+=c[g[0]]
    #     a1.pop()
    #     for x in range(n-1,g[0]-1,-1):
    #         if c[x]<=k:
    #             a1.append((x,1))
    #             break
    #     a1.append((g[0],g[1]-1))
    # # print(a1)


    # ans = [0]*(n+1)
    # for x in a1:
    #     ans[0]+=x[1]
    #     ans[x[0]+1]-=x[1]
    
    # for x in range(1,n):
    #     ans[x]+=ans[x-1]
    
    # printl(ans[:n])
    

    for x in range(n-2,-1,-1):
        c[x] = min(c[x],c[x+1])
    
    # print(c)
    a1 = [0]*n
    a1[0] = k//c[0]
    k -= a1[0]*c[0]
    for x in range(1,n):
        if c[x]==c[x-1]:
            a1[x] = a1[x-1]
            a1[x-1] = 0
        else:
            ch = min(a1[x-1],k//(c[x]-c[x-1]))
            a1[x-1]-=ch
            a1[x] = ch
            k -= ch*(c[x]-c[x-1])
    for x in range(n-2,-1,-1):
        a1[x]+=a1[x+1]
    printl(a1)




    



for _ in range(int(input())):
    solve()