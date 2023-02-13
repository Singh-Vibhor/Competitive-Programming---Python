ans=""
l=[]
for x in range(int(input())):
    l.append(input())
#print(l)
for x in range(int(input())):
    a,b,c=list(map(int,input().split()))
    d=l[b-1][len(l[b-1])-a:]
    l[c-1]+=d[::-1]
    l[b-1]=l[b-1][:len(l[b-1])-a]
    if l[b-1]==" ":
        l[b-1]=""
print(l)

for x in l:
    ans+=x[len(x)-1]
print(ans)