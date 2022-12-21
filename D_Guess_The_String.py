import sys
n=int(input())
a=[]
for x in range(n-1):
    print("? 2",x+1,x+2)
    sys.stdout.flush()
    c=int(input())
    if c!=1:
        a.append(x+2)
    
s=""

print("? 1 1")
sys.stdout.flush()
s+=input()*(a[0]-1)
for x in range(len(a)):
    print("? 1",a[x])
    sys.stdout.flush()
    if x!=(len(a)-1):
        s+=input()*(a[x+1]-a[x])
    else:
        s+=input()*(n-a[x]+1)

print("!",s)
