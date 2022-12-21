for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    
    else:
        if n%2:
            print(2,3,1, end=" ")
            for x in range(4,n+1,2):
                print(x+1,x,end=" ")
            
            print()
        else:
            for x in range(1,n+1,2):
                print(x+1,x,end=" ")
            print()
