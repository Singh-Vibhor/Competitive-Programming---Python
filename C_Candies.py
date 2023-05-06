n = int(input())
l=list(map(int,input().split()))
prf = [0]
for x in range(n):
    prf.append(l[x]+prf[x])
prf.append(0)

for _ in range(int(input())):
    l,r = list(map(int,input().split()))
    #print(prf)
    print((prf[r]-prf[l-1])//10)