for _ in range(int(input())):
    n=int(input())
    if n%2:
        for x in range(n):
            print(1, end=" ")
        print()
    else:
        if n==2:
            print(1,3)
        else:
            print(1,3,2,end=" ")
            n-=3
            for x in range(n):
                print(2, end=" ")
            print()