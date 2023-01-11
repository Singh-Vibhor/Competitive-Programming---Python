for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("YES")
        print(1)
    elif n%2==1:
        print("NO")
    else:
        print("YES")
        for x in range(n):
            if x%2:
                print(5000,end=" ")
            else:
                print(-5000,end=" ")
        print()
    

