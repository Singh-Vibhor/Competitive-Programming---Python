s = input()
n = int(input())
m = int(s[3:])
h = int(s[:2])
m+=n
h+=m//60
m%=60
h%=24
m = str(m)
h = str(h)
if len(m)==1:
    m = '0'+m
if len(h)==1:
    h = '0'+h
print(h+":"+m)
