for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    ad=l[0]
    ar=l[0]

    for x in range(1,n):
        ad=ad & l[x]
        ar=ar | l[x]

    print(ar-ad) 