import math
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1 = sorted(l)
    d=defaultdict(int)
    for x in range(n):
        d[l[x]] = x
    
    ans = d[l1[0]]
    for x in range(n):
        ans = math.gcd(ans,abs(d[l1[x]]-x))
    print(ans)
