def dfs(s):
    visited_dfs[s] = 1
    stack = []
    while True:
        for w in sorted(nodes[s]):
            if visited_dfs[w] == 0:
                stack.append(s)
                res_dfs.append(w)
                s = w
                dfs(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                return

def bfs(s):
    visited_bfs[s] = 1
    stack = [s]
    while stack:
        s = stack.pop(0)
        for w in sorted(nodes[s]):
            if visited_bfs[w] == 0:
                stack.append(w)
                res_bfs.append(w)
                visited_bfs[w] = 1


N, M, V = map(int, input().split())

nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i)

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
res_dfs = [V]
res_bfs = [V]
dfs(V)
bfs(V)

print(*res_dfs)
print(*res_bfs)