from math import gcd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    gd=l[0] 
    for x in l:
        gd=gcd(x,gd)
    
    if gd==1:
        print(0)
    
    else:
        a=gcd(n,l[n-1])
        b=gcd(n-1,l[n-2])   
        gd1=l[0]
        for x in range(n):
            if x==n-1:
                gd=gcd(gd,a)
            else:
                gd=gcd(gd,l[x])
            
            if x==n-2:
                gd1=gcd(gd1,b)
            else:
                gd1=gcd(gd1,l[x])
            
        if gd==1:
            print(1)
        elif gd1==1:
            print(2)
        else:
            print(3)