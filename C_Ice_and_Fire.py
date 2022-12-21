for _ in range(int(input())):
    n=int(input())
    s=input()
    print(1,end=" ")
    cnt=1
    for x in range(1,n-1):
        if s[x]==s[x-1]:
            cnt+=1
        else:
            cnt=1
        print(x-cnt+2,end=" ")
    print()