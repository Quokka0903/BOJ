from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

ik = deque()
cnt = 0
wall = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                ik.append((z, y, x))
                cnt += 1
            elif tomato[z][y][x] == -1:
                wall += 1

ans = 0
if cnt + wall == N * M * H:
    pass

else:
    res = []
    while ik and cnt + wall != N * M * H:
        sz, sy, sx = ik.popleft()
        for dz, dy, dx in [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
            nz, ny, nx = sz + dz, sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = tomato[sz][sy][sx] + 1
                    ans = tomato[sz][sy][sx] + 1
                    cnt += 1
                    ik.append((nz, ny, nx))
                    #print(tomato)
    ans -= 1

if cnt + wall == N * M * H:
    print (ans)
else: 
    print (-1)