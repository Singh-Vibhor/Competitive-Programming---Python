import math
for _ in range(int(input())):
    n,l,r=list(map(int,input().split()))
    flag=True
    l1=[]
    for x in range(1,n+1):
        y=(math.ceil(l/x))*x+x
        if y<=r:
            l1.append(y)
        else:
            print("NO")
            break

        if len(l1)==n:
            print("YES")
            print(" ".join(map(str,l1)))
    