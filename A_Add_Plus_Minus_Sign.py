for _ in range(int(input())):
    n=int(input())
    s=input()
    a=0
    ans=""
    for x in range(1,n):
        if s[x]=='0':
            ans+='+'
        elif a==0:
            ans+='-'
            a=1-a
        else:
            ans+='+'
            a=1-a
    print(ans)