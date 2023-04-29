for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    mx=max(l1[n-1],l2[n-1])
    mn=min(l1[n-1],l2[n-1])
    ans="YES"
    for x in range(n):
        if max(l1[x],l2[x])>mx or min(l1[x],l2[x])>mn:
            ans="NO"
            break
    
    print(ans)
