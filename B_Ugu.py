for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    f=0
    f1=0
    for x in range(n):
        if s[x]=='0' and f1==0:
            continue
        elif f1==0:
            f1=1
            continue
        

        if s[x]=='0' and s[x-1]=='1':
            ans+=1
        
        if s[x]=='1' and s[x-1]=='0':
            ans+=1
        
    print(ans)