for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=True
    for x in range(1,n):
        if l[x]%l[0]!=0:
            flag=False
            break

    if flag:
        print("YES")
    else:
        print("NO")