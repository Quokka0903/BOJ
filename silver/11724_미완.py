N, M = map(int, input().split())
nodes = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [0] * (N + 1)
union = 0
for i in range(1, N + 1):
    q = []
    if visited[i] == 0:
        union += 1
        visited[i] = union
        q.append(i)
    while q:
        s = q.pop(0)
        for w in nodes[s]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = union

print(visited)
print(union)