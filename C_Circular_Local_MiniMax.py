for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if n%2==1:
        print("NO")
    else:
        ans=[]
        fg=True
        m=int(n/2)
        for x in range(m):
            if a[x]==a[x+m-1] and x!=0:
                print("NO")
                fg=False
                break
            ans.append(a[x])
            ans.append(a[x+m])
        
        if fg:
            print("YES")
            print(" ".join(map(str,ans)))
            