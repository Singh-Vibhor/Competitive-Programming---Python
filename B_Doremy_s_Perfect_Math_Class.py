import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a=l[0]
    for x in l:
        a=math.gcd(a,x)
    print(int(l[n-1]/a))
            