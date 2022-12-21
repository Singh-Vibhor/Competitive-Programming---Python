for _ in range(int(input())):
    n,y=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    a1=-1
    a2=-1
    s=0
    arr=arr[::-1]
    
    for x in range(n):
        if arr[x]>=0:
            s=s+arr[x]
        elif arr[x]<=-y:
            if a1==-1:
                a1=x
            a2=x
            break
        elif a1==-1:
            a1=x

    if a1!=-1 and a2!=-1:
        for x in range(a1+1):
            print(s+(y*x), end="")
            print(" ",end="")
        s=s+(y*(a1-1))
        


        for x in range(a1,a2):
            s=s+y+arr[x]
            print(s,end="")
            print(" ",end="")

        for x in range(a2,n):
            print(s,end="")
            print(" ",end="")

    elif a2==-1 and a1!=-1:
        for x in range(a1+1):
            print(s+(y*x), end="")
            print(" ",end="")

        s=s+(y*a1)


        for x in range(a1,n):
            s=s+y+arr[x]
            print(s,end="")
            print(" ",end="")

    else:
        for x in range(n+1):
            print(s+(y*x), end="")
            print(" ",end="")

