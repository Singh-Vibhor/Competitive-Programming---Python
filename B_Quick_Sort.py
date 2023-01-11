import math
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ans=0
    shift=-1
    for x in range(n):
        if l[x]!=x-shift:
            shift+=1
            ans+=1
    print(math.ceil(ans/k))