for _ in range(int(input())):
    n=int(input())

    for x in range(1,n+1):
        
        for y in range(x):
            if y==0:
                print(1,end=" ")
            elif y==x-1:
                print(1,end=" ")
            
            else:
                print(0, end=" ")
            
        print()
