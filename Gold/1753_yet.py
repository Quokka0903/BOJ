import sys, collections
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

nodes = [[] for _ in range(V + 1)]

for _ in range(E):
    n1, n2, val = map(int, input().split())
    nodes[n1].append([n2, val])
visited = [-1] * (V + 1)

stack = collections.deque([K])
visited[K] = 0
while stack:
    s = stack.popleft()

    for node, val in nodes[s]:
        if visited[node] == -1 or visited[s] + val < visited[node]:
            visited[node] = visited[s] + val
            stack.append(node)

for i in range(1, V + 1):
    if visited[i] == -1:
        print('INF')
    else:
        print(visited[i])