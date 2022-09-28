from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

ik = deque()
cnt = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                ik.append((z, y, x))
                cnt += 1

res = []
while ik:
    sz, sy, sx = ik.popleft()
    for dz, dy, dx in [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
        if 0 <= sy + dy < N and 0 <= sx + dx < M and 0 <= sz + dz < H:
            if tomato[sz + dz][sy + dy][sx + dx] == 0 or tomato[sz + dz][sy + dy][sx + dx] > tomato[sz][sy][sx] + 1:
                tomato[sz + dz][sy + dy][sx + dx] = tomato[sz][sy][sx] + 1
                ik.append((sz + dz, sy + dy, sx + dx))

def chk():
    ans = -1
    for z in range(H):
        for y in range(N):
            if 0 in tomato[z][y]:
                print(-1)
                return
            for x in range(M):
                if tomato[z][y][x] > ans:
                    ans = tomato[z][y][x]

    else:
        print(ans - 1)
        return
chk()