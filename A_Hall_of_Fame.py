for _ in range(int(input())):
    n=int(input())
    s=input()
    fl=0
    fr=0
    flr=0
    for x in s:
        if x=='L':
            fl=1
        
        if x=='R':
            fr=1
        
        if fr and x=='L':
            flr=1
            break
    
    if fr==0 or fl==0:
        print(-1)
    
    else:
        if flr:
            print(0)
        else:
            for x in range(n):
                if s[x]=='R':
                    print(x)
                    break

