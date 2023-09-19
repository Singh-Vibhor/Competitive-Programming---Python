div = 5
ans = 0
n=int(input())
while div<=n:
    ans+=n//div
    div*=5
print(ans)