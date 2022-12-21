import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(n)
    for x in range(n):
        print(x+1, end=" ")
        ans=int(math.pow(2,math.ceil(math.log(l[x],2))))-l[x]
        print(ans)
    
    