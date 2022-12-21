from collections import Counter as ct
for _ in range(int(input())):
    n=int(input())
    l=input().split()
    d1=ct(l)
    l1=list(d1.values())

    l2=len(l1)
    for x in range(l2):
        print(l2, end="")
        print(" ",end="")
        
    for x in range(l2+1,n+1):
        print(x,end="")
        print(" ",end="")

    print("")



