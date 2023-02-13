from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=dd(list)
    for x in range(n):
        d[a[x]].append(x+1)

    print(d)
