n=int(input())
s = input()
cnt = 0
for x in s:
    if x == '1':
        cnt+=1
if cnt==n-cnt:
    print(2)
    print(s[0], s[1:])
else:
    print(1)
    print(s)