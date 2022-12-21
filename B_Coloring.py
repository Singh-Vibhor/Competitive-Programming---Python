import math
from collections import Counter
for _ in range(int(input())):
    n,m,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    a=max(l)
    c=Counter(l)
    c1=c[a]
    #print(c,c1)
    if a>int((n+k-1)/k):
        print("NO")
    elif n%k:
        if a==int((n+k-1)/k) and c1>n%k:
            print("NO")
        else:
            print("YES")

    else:
        print("YES")