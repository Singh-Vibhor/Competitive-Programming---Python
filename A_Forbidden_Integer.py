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
    n,k,x = linput()
    if k==1 and x==1:
        print("NO")
        return
    elif x==1 and n==1:
        print("NO")
        return

    if k==2 and x==1 and n%2:
        print("NO")
        return
    
    print("YES")

    if x==1:
        
        if n%2:
            print(1+(n-3)//2)
            print(3, end = " ")
            for x in range((n-3)//2):
                print(2, end = " ")
        else:
            print(n//2)
            for x in range(n//2):
                print(2,end = " ")
    else:
        print(n)
        for x in range(n):
            print("1", end = " ")
    print()



for _ in range(int(input())):
    solve()