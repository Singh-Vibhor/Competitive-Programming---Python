#work around bits
import math
for _ in range(int(input())):
    n=int(input())
    if n==1 or n==2:
        print(3)
    elif math.ceil(math.log2(n))==math.floor(math.log2(n)):
        print(n+1)
    else:
        pw=0
        while n>0:
            if n%2==1:
                break
            n/=2
            pw+=1
        print(int(math.pow(2,pw)))