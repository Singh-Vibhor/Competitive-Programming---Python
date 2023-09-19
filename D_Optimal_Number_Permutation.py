n=int(input())
l=[n]*(2*n)
for x in range(1,n+1):
    if x%2:
        a = x>>1
    else:
        a = n-1+(x>>1)
    b = a + (n-x)
    l[a] = x
    l[b] = x
print(" ".join(map(str,l)))