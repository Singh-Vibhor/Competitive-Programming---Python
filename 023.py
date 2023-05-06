from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# @bootstrap
def dfs(x, y):
    # l[x][y] = '#'
    # if x+1<n and l[x+1][y]!='#':
    #     yield dfs(x+1,y)
    
    # if x-1>=0 and l[x-1][y]!='#':
    #     yield dfs(x-1,y)

    # if y+1<m and l[x][y+1]!='#':
    #     yield dfs(x,y+1)

    # if y-1>=0 and l[x][y-1]!='#':
    #     yield dfs(x,y-1)
    stk = []
    stk.append((x,y))
    while len(stk):
        crr = stk.pop()
        x = crr[0]
        y= crr[1]
        l[x][y] = '#'
        if x+1<n and l[x+1][y]!='#':
            stk.append((x+1,y))
        
        if x-1>=0 and l[x-1][y]!='#':
            stk.append((x-1,y))

        if y+1<m and l[x][y+1]!='#':
            stk.append((x,y+1))

        if y-1>=0 and l[x][y-1]!='#':
            stk.append((x,y-1))



n,m = list(map(int,input().split()))
l = []
for x in range(n):
    l.append([*input()])

ans = 0

for x in range(n):
    for y in range(m):
        if l[x][y]=='#':
            continue
        dfs(x,y)
        ans+=1


print(ans)
