from collections import defaultdict as dd
n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
sm=sum(a)
prv=-1
flag=0
d=dd(int)
for _ in range(q):
    qr=list(map(int,input().split()))
    
    

    if qr[0]==2:
        sm=n*qr[1]
        prv=qr[1]
        print(sm)
        flag=1
        d=dd(int)
    
    elif (qr[0]==1) and (flag==0):
        sm=sm-a[qr[1]-1]+qr[2]
        print(sm)
    
    else:
        if d[qr[1]-1]==0:
            d[qr[1]-1]=qr[2]
            sm=sm-prv+qr[2]
            print(sm)
        
        else:
            sm=sm-d[qr[1]-1]+qr[2]
            d[qr[1]-1]=qr[2]

