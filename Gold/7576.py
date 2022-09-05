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

days = 1
while ik:
    s = ik.popleft()
    

