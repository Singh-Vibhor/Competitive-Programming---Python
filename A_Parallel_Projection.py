for _ in range(int(input())):
    w,d1,h=list(map(int,input().split()))
    a,b,c,d=list(map(int,input().split()))
    ans=0
    ans+=h+abs(a-c)
    ans+=min(b+d,2*d1-b-d)
    ans1=0
    ans1+=h+abs(b-d)
    ans1+=min(a+c,2*w-a-c)
    print(min(ans,ans1))
