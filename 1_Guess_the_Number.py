import sys
a=1
b=1000000
while(b>a):
    mid=int((a+b+1)/2)
    print(mid)
    sys.stdout.flush()
    
    c=input()
    if c==">=":
        a=mid
    else:
        b=mid-1
    
print("!",a)