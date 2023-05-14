for _ in range(int(input())):
    n=int(input())
    if n%2:
        print(" ".join(map(str,range(1,n+1))))
    else:
        for x in range(1,n+1):
            print(2*x, end = " ")
        print()