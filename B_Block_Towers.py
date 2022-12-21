for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    l.sort()
    for x in l:
        if x>a:
            a+=int((x-a+1)/2)
        
    print(a)