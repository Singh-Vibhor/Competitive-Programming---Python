from collections import defaultdict as dd
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    d=dd(int)
    for x in l:
        if d[x-1]==0 and x<=int((m+1)/2):
            d[x-1]=1
        
        elif d[m-x]==0:
            d[m-x]=1

        else:
            d[x-1]=1

    for x in range(m):
        if d[x]==0:
            print("B",end="")
        else:
            print("A",end="")
    print()