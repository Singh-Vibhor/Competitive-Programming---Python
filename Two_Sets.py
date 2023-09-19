n=int(input())
if n%4==0:
    ans1 = []
    ans2 = []
    crr = 1
    while crr<n:
        ans1.extend([crr,crr+3])
        ans2.extend([crr+1,crr+2])
        crr+=4
    print("YES")
    print(len(ans1))
    print(" ".join(map(str,ans1)))
    print(len(ans2))
    print(" ".join(map(str,ans2)))

elif n%4==3:
    ans1 = [1,2]
    ans2 = [3]
    crr = 4
    while crr<n:
        ans1.extend([crr,crr+3])
        ans2.extend([crr+1,crr+2])
        crr+=4
    print("YES")
    print(len(ans1))
    print(" ".join(map(str,ans1)))
    print(len(ans2))
    print(" ".join(map(str,ans2)))

else:
    print("NO")
