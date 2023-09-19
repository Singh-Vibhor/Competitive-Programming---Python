from collections import Counter
s=input()
c = Counter(s)
od = 0
g = ""
for y,x in c.items():
    # print(x,y,od)
    if x%2:
        od+=1
        g = y
if od>1:
    print("NO SOLUTION")
else:
    ans = ""
    for y,x in c.items():
        ans+=y*(x//2)
    print(ans+g+ans[::-1])
