for _ in range(int(input())):
    n=int(input())
    s=input()
    r=n
    c=0
    x=0
    while x<(n-1):
        if s[x]=="(":
            x=x+2
            c=c+1
            r=n-x
        
        elif s[x]==")" and s[x+1]==")":
            x=x+2
            c=c+1
            r=n-x

        else:
            a=s.find(")",x+1,n)
            if a=="-1":
                break
            else:
                x=a+1
                print(x)
                c=c+1
                r=n-x
    print(c,r)

