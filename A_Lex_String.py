for _ in range(int(input())):
    n1,n2,k=list(map(int,input().split()))
    a=input()
    b=input()
    p1=0
    p2=0
    ans=""
    a=sorted(a)
    b=sorted(b)
    cta=0
    ctb=0
    while(True):
        if cta==k:
            ans+=b[p2]
            p2+=1
            cta=0
            ctb=1
        
        elif ctb==k:
            ans+=a[p1]
            p1+=1
            ctb=0
            cta=1
        
        else:
            if a[p1]>b[p2]:
                ans+=b[p2]
                ctb+=1
                cta=0
                p2+=1
            elif a[p1]<b[p2]:
                ans+=a[p1]
                cta+=1
                ctb=0
                p1+=1
            else:
                if (n1-p1)<(n2-p2):
                    ans+=a[p1]
                    cta+=1
                    ctb=0
                    p1+=1
                else:
                    ans+=b[p2]
                    ctb+=1
                    cta=0
                    p2+=1
        if p1==n1 or p2==n2:
            break
    print(ans)
                    

        

