for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ne=0
    no=0
    for x in range(n):
        if a[x]%2==0:
            ne+=1
        else:
            no+=1
        
    print(min(ne,no))
