m,a,b = list(map(int,input().split()))
if a+b==2*m and a%2:
    print(1,min(m,a,b))
else:
    print(0,min(m,a,b))