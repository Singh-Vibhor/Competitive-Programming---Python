for _ in range(int(input())):
    n=int(input())
    a=1
    b=n*n
    s1=0
    crr=-1
    l=[[0]*n for x in range(n)]
    while True:
        crr+=1
        if s1==0:

            for x in range(n):
                if x%2:
                    l[crr][x]=b
                    b-=1
                else:
                    l[crr][x]=a
                    a+=1
        else:
            for x in range(n-1,-1,-1):
                if x%2==0:
                    l[crr][x]=b
                    b-=1
                else:
                    l[crr][x]=a
                    a+=1
        s1=1-s1
        if crr==n-1:
            break
    for x in range(n):
        print(" ".join(map(str,l[x])))

