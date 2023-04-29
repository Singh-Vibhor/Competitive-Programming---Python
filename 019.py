import functools
m1, m2, m3, m4, m5 = {}, {}, {}, {}, {}
v=[]

def comp(a,b):
  if int(m1[a]>m1[b]) + int(m2[a]>m2[b]) + int(m3[a]>m3[b]) + int(m4[a]>m4[b]) + int(m5[a]>m5[b]) >=3:
    return 1
  return -1

n=int(input())
for z in range(5):
  for x in range(n):
    y=int(input())
    if z==0:
      m1[y]=x
    if z==1:
      m2[y]=x
    if z==2:
      m3[y]=x
    if z==3:
      m4[y]=x
    if z==4:
      m5[y]=x
      v.append(y)

v.sort(key = functools.cmp_to_key(comp))
for x in v:
  print(x)