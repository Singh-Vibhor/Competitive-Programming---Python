for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    if n%2:
        print(-1)
    else:
        ans=[]
        for x in range(0,n,2):
            if l[x]!=l[x+1]:
                ans.extend([[x+1,x+1],[x+2,x+2]])
            else:
                ans.append([x+1,x+2])
            
        print(len(ans))
        for x in ans:
            print(x[0],x[1])