from collections import *
from itertools import *
from functools import *
from heapq import *
import sys,math
input = sys.stdin.readline

# cook your dish here
#I AM SAD SCAM

# 5 2 
# 2 1 3 5 4 
# 4 5 3 1 2 

# 5 3 
# 7 4 
# 7 2 
# 2 1 5 4 3 7 6
# 3 2 1 4 7 6 5

# 6 2
# 2 1 3 5 4 6
# 3 2 1 6 5 4


for _ in range(int(input())):

    n,x = list(map(int,input().split()))
    
    if n%2 and x==(n+1)//2:
        print(-1)
        continue
    
    a = []
    
    for i in range(n):
        a.append(i+1)
    
    if x==n :
        for i in a[::-1]:
            print(i,end=' ')
        print()
        continue
    if x==1 :
        for i in a:
            print(i,end=' ')
        print()
        continue

    t = a[0]
    a[0] = a[x-1]
    a[x-1] = t  
    
    t = a[n-1]
    a[n-1] = a[n-x]
    a[n-x] = t
    
    for i in a:
        print(i,end=' ')

    print()
        
        
    
    
    
    
    
    
    