import math

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sm=sum(a)
    flg=False
    for x in a:
        s1=sm-x
        if  math.ceil(s1/(n-1))==math.floor(s1/(n-1)):
            if int(s1/(n-1))==x:
                flg=True
                break
        
    if flg:
        print("YES")
    else:
        print("NO")