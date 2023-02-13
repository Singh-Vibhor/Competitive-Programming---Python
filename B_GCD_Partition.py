def gcd(x,y):
    while y:
        x, y = y, x % y
    return abs(x)

for x in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    sm=sum(l)
    crr=0
    mx=0
    for x in l[:n-1]:
        crr+=x
        mx=max(gcd(crr,sm-crr),mx)
    print(mx)

