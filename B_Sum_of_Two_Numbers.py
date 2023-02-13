def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
for _ in range(int(input())):
    n=int(input())
    f = 0
    if n%2==0:
        print(n//2,n//2)
    else:
        a = ""
        b = ""
        n=str(n)

        for x in n:
            x=int(x)
            if x%2:
                if f:
                    a+=str(x//2)
                    b+=str((x+1)//2)
                    f = 1-f
                else:
                    a+=str((x+1)//2)
                    b+=str(x//2)
                    f = 1-f
            else:
                a+=str(x//2)
                b+=str(x//2)
        print(int(a),int(b))