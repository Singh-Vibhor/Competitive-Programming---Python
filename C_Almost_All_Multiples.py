for x in range(int(input())):
    n,x=list(map(int,input().split()))
    if n%x!=0:
        print(-1)
    else:
        print(x,end=" ")

        for y in range(2,n):
            if y==x:
                f=1
                a=2
                while(x*a<=n):
                    if n%(x*a)==0:
                        print(x*a, end=" ")
                        x=x*a
                        f=0
                        break
                    a+=1
                if f:
                    print(n,end=" ")
            else:
                print(y, end=" ")
        print(1)

