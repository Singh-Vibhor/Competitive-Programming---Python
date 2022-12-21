# cook your dish here
def appender(d,a):
    for y in range(97,122):
        ch=chr(x)
        if ch==a:
            continue
        else:
            d[ch].append()
            
        return d

from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    s=input()
    d=dd(list)
    crr=1
    for x in range(n-1):
        if s[x]==s[x+1]:
            crr+=1
        
        else:
            d[s[x]].append(crr)
            crr=1
            d=appender(d,s[x])
            
    d[s[n-1]].append(crr)
    d=appender(d,s[x])
    
    for x in range(97,122):
        print(d[chr(x)])
    
    
    