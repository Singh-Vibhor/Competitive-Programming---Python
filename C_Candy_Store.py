import math
for _ in range(int(input())):
    n=int(input())
    ans = 1
    a1, b1 = list(map(int,input().split()))
    crrgcd = a1*b1
    crrlcm = b1

    for x in range(n-1):
        a, b = list(map(int,input().split()))
        crrgcd = math.gcd(crrgcd,a*b)
        crrlcm = int((crrlcm*b)/math.gcd(crrlcm,b))

        if crrgcd % crrlcm != 0:
            crrgcd = a*b
            crrlcm = b
            ans+=1
    
    print(ans)