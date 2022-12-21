import math

n=int(input())
s=input()
es=0
el=0
for x in s:
    if x=='1':
        es+=1
    else:
        el+=1

for x in range(int(math.pow(2,es)),int(math.pow(2,n))-int(math.pow(2,el))+2):
    print(x, end=" ")
print()