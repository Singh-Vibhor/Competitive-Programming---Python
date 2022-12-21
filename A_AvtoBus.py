import math
for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        print(-1)
    elif n==2:
        print(-1)
    else:
        x=math.ceil(n/6)
        y=math.floor(n/4)
        print(min(x,y),max(x,y))