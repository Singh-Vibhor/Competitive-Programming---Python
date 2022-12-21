import math
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    a=x*x+y*y
    #print(a)
    #print(int(math.sqrt(x^2+y^2)))
    #print(int(math.ceil(math.sqrt(x^2+y^2))))
    if x==0 and y==0:
        print("0")
    elif int(math.sqrt(a))==int(math.ceil(math.sqrt(a))):
        print("1")
    else:
        print("2")