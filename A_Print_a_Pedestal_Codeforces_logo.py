for _ in range(int(input())):
    n=int(input())
    a=int(n/3)
    if n%3==0:
        print(a,a+1,a-1)
    elif n%3==1:
        print(a,a+2,a-1)
    else:
        print(a+1,a+2,a-1)