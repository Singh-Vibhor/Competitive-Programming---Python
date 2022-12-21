from collections import defaultdict as dd
from collections import Counter as ct

for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    d=dd(int)
    d=ct(l)
    flag=False
    for x in d.keys():
        num=x-k
        if d[num]!=0:
            print("YES")
            flag=True
            break
        
    if flag==False:
        print("NO")

    