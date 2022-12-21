for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l1=[]
    l2=[]
    for x in range(n):
        if a[x]==0:
            l1.append(b[x])
        else:
            l2.append(b[x])
    
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    