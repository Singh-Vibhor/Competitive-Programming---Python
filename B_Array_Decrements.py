for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    flag=True
    n1=-1
    for x in range(n):
        if b[x]!=0:
            n1=x
            break
    if n1==-1:
        print("YES")
    else:
        dif=a[n1]-b[n1]
        for x in range(n):  
            if a[x]<b[x]:
                flag=False
                break
            if b[x]==0:
                if a[x]>dif:
                    flag=False
                    break
            elif a[x]-b[x]!=dif:
                flag=False
                break
    
        if flag:
            print("YES")
        else:
            print("NO")
