import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

nodes = [[] for _ in range(V + 1)]

for _ in range(E):
    n1, n2, val = map(int, input().split())
    nodes[n1].append([val, n2])
visited = [10**6] * (V + 1)

hq = [[0, K]]
visited[K] = 0
while hq:
    w, s = heapq.heappop(hq)

    if visited[s] < w:
        continue

    for val, node in nodes[s]:
        if visited[s] + val < visited[node]:
            visited[node] = visited[s] + val
            heapq.heappush(hq, [visited[s] + val, node])

for i in range(1, V + 1):
    if visited[i] == 10**6:
        print('INF')
    else:
        print(visited[i])