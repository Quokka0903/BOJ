import sys
sys.setrecursionlimit(10**7)

T = int(input())

def dfs(V):
    visited[V] = 1 
    next = perm[V]
    
    if visited[next] == 0: 
        dfs(next)

for i in range(T):
    N = int(input())
    perm = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    res = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)
            res += 1

    print(res) 