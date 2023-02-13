for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    if l[0]==l[n-1]:
        print("NO")
    else:
        print("YES")
        print(l[n-1],l[0],end=" ")
        for x in range(1,n-1):
            print(l[x],end=" ")
        print()