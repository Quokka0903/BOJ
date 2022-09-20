from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

ik = deque()
cnt = 0
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            ik.append((y, x))
            cnt += 1

res = []
while ik:
    sy, sx = ik.popleft()
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= sy + dy < N and 0 <= sx + dx < M:
            if tomato[sy + dy][sx + dx] == 0 or tomato[sy + dy][sx + dx] > tomato[sy][sx] + 1:
                tomato[sy + dy][sx + dx] = tomato[sy][sx] + 1
                ik.append((sy + dy, sx + dx))

ans = -1
for y in range(N):
    if 0 in tomato[y]:
        print(-1)
        break
    for x in range(M):
        if tomato[y][x] > ans:
            ans = tomato[y][x]

else:
    print(ans - 1)