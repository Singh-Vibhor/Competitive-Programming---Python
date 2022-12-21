for _ in range(int(input())):
    n,a,b=list(map(int,input().split()))
    x=min(a,b)
    y=max(a,b)
    if x!=0:
        print(-1)
    elif y==0:
        print(-1)
    
    else:
        if (n-1)%y!=0:
            print(-1)
        elif y==1:
            print(1,end=" ")
            print(" ".join(map(str,range(3,n+1))))
        else:
            ans=[]
            ans.extend([1]*y)

            for x in range(y+2,n,y):
                ans.extend([x]*y)
            
            print(" ".join(map(str,ans)))

