def dfs(v, lists):

    cnt = 0
    infected[v] = 1
    while True:
        for w in lists[v]:

            if infected[w] == 0:
                stack.append(v)
                v = w
                infected[w] = 1
                cnt += 1
                
                print(v)
                print(stack)
                print(infected)
                break

        else :
            if stack:
                v = stack.pop()
            else:
                break
    
    return cnt

N = int(input())
M = int(input())

coms = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b  = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

stack = []
infected = [0] * (N + 1)
print(coms)
print(dfs(1, coms))