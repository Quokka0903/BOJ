import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chingu = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    chingu[a].append(b)
    chingu[b].append(a)

min_hap = N * N
ans = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    stack = [[i, 0]]
    while stack:
        n, cnt = stack.pop()
        for unit in chingu[n]:
            if unit == i:
                continue
            if visited[unit] == 0 or cnt + 1 < visited[unit]:
                visited[unit] = cnt + 1
                stack.append([unit, cnt + 1])

    if min_hap > sum(visited):
        min_hap = sum(visited)
        ans = i

print(ans)