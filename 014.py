from __future__ import absolute_import
from xmlrpc.client import NOT_WELLFORMED_ERROR


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=[[0]*n]*32
    #print(l)
    for i in range(32):
        g=0
        for j in range(n):
            if a[j]%2==1:
                g+=1
            l[i][j]=g
            a[j]>>1
    
    for q1 in range(int(input())):
        q=list(map(int,input().split()))
        
        

