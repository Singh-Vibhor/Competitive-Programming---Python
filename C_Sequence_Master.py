for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    if n==1:
        ans = min(abs(l[0]-l[1]),abs(l[0])+abs(l[1]))
    
    elif n==2:
        ans1 = sum(map(abs,l))
        ans2 = abs(l[0]-2)+abs(l[1]-2)+abs(l[2]-2)+abs(l[3]-2)
        ans = 0
        for x in l:
            ans+=abs(x+1)
        ans3 = ans
        for x in l:
            ans3 = min(ans3,ans-abs(x+1)+abs(x-n))
        ans = min(ans1,ans2,ans3)
    
    else:
        ans1 = sum(map(abs,l))
        ans = 0
        for x in l:
            ans+=abs(x+1)
        ans3 = ans
        for x in l:
            ans3 = min(ans3,ans-abs(x+1)+abs(x-n))
        ans = min(ans1,ans3)
    print(ans)
