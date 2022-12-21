for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    s1=input()
    s2=input()
    a=0
    b=0
    f="NO"
    while a<n:
        if s1[a]==s2[b]:
            b+=1
        a+=1
        if b==m:
            f="YES"
            break
    
    print(f)