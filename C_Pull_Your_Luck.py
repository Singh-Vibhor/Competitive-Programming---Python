def f(n,x,p):
    for i in range(1,min(2*n,p) + 1):
        if (((i*(i+1))/2)+x)%n==0:
            return "Yes"
    return "No"    

for _ in range(int(input())):
    n, x, p = list(map(int,input().split()))
    print (f(n,x,p))