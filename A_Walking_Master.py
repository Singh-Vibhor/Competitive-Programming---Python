for _ in range(int(input())):
    a, b, c ,d = list(map(int,input().split()))
    
    if c-a > d-b or b>d:
        print(-1)
    
    else:
        ans = 2*(d-b)+a-c
        print(ans)
