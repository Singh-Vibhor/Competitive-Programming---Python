s=input()
crr = 1
prv = ""
ans = 1
for x in s:
    if x==prv:
        crr+=1
    else:
        ans = max(ans,crr)
        crr=1
    prv = x
print(max(ans,crr))