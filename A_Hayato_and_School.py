from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=dd(list)
    for x in range(n):
        d[l[x]%2].append(x+1)
    
    if len(d[1])>=1 and len(d[0])>=2:
        print("YES")
        print(d[0][0],d[0][1],d[1][0])
    elif len(d[1])>=3:
        print("YES")
        print(d[1][0],d[1][1], d[1][2])
    else:
        print("NO")