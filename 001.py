for _ in range(int(input())):
    n=int(input())
    l=['1','3','2','4']
    while len(l)>n:
        l.pop()

    for x in range(5,n+1):
        l.append(str(x))
    if n==3:
        print("1 3 2")
        print("3 2 1")
        print("3 1 2")

    else: 
        for x in range(n):
            print(' '.join(l[x:])+" "+" ".join(l[:x]))
