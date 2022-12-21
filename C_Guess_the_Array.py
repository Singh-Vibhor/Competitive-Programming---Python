import sys
n=int(input())
s=0
def smt(a,b,c):
    a1=a-c
    a2=a1+b
    q=int(a2/2)
    r=b-q
    p=a-q

    return [p,q,r]
ans=[]

a=[0,0,0]
print("?",1,2)
sys.stdout.flush()
a[0]=int(input())
    
print("?",2,3)
sys.stdout.flush()
a[1]=int(input())
    
print("?",1,3)
sys.stdout.flush()
a[2]=int(input())

a=smt(a[0],a[1],a[2])
ans.append(a[0])
ans.append(a[1])
ans.append(a[2])
#print(n)
for x in range(4,n+1):
    print("? 1",x)
    sys.stdout.flush()
    s=int(input())
    ans.append(s-a[0])

print("!"," ".join(map(str,ans)))


    
