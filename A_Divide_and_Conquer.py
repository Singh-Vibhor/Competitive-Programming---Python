for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if sum(l)%2==0:
        ans=0
    else:
        ans=1000000
        for x in l:
            if x%2:
                n1=0
                while(x%2):
                    n1+=1
                    x=x//2
                ans=min(ans,n1)
            else:
                n1=0
                while x%2==0:
                    n1+=1
                    x=x//2
                ans=min(ans,n1)
    
    print(ans)